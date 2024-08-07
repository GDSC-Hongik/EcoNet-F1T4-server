from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from .models import Gathering, Comment
from .serializers import GatheringSerializer, GatheringDetailSerializer, CommentCreateSerializer, GatheringCreateSerializer, GatheringUpdateSerializer

@api_view(['GET', 'POST'])
def gathering_list_create(request):
    if request.method == 'GET':
        page = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 10)

        try:
            page = int(page)
            limit = int(limit)
        except ValueError:
            return Response({"error": "페이지나 로드 수가 적절하지 않습니다"}, status=status.HTTP_400_BAD_REQUEST)

        offset = (page - 1) * limit
        gatherings = Gathering.objects.all()[offset:offset + limit]
        serializer = GatheringSerializer(gatherings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"error": "먼저 사용자 인증이 필요합니다!"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = GatheringCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def gathering_detail_update_delete(request, gatheringpost_id):
    try:
        gathering = Gathering.objects.get(id=gatheringpost_id)
    except Gathering.DoesNotExist:
        return Response({"error": "모임이 존재하지 않습니다"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GatheringDetailSerializer(gathering)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = GatheringUpdateSerializer(gathering, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gathering.delete()
        return Response({"message": "모임이 삭제되었습니다."}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_comment(request, gatheringpost_id):
    try:
        gathering = Gathering.objects.get(id=gatheringpost_id)
    except Gathering.DoesNotExist:
        return Response({"error": "모임이 존재하지 않습니다"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(gathering=gathering, date=date.today())
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)