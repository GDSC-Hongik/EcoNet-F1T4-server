from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Bin, MapoDistrict
from .serializers import BinSerializer, MapoDistrictSerializer, BinDetailSerializer, PictureSerializer, InformationSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def bin_list(request):
    if request.method == 'GET':
        bins = Bin.objects.all()
        bin_serializer = BinSerializer(bins, many=True)
        
        mapo_districts = MapoDistrict.objects.all()  # 모든 MapoDistrict 데이터 가져오기
        mapo_district_serializer = MapoDistrictSerializer(mapo_districts, many=True)  # 직렬화
        
        response_data = {
            "bins": bin_serializer.data,
            "mapo_districts": mapo_district_serializer.data 
        }
        return Response(response_data)

@api_view(['GET'])
@permission_classes([AllowAny])
def bin_detail(request, pk):
    try:
        bin = Bin.objects.get(pk=pk)
    except Bin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        bin_serializer = BinDetailSerializer(bin)
        return Response(bin_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_picture(request, pk):
    try:
        bin_instance = Bin.objects.get(pk=pk)
    except Bin.DoesNotExist:
        return Response({"detail": "Bin not found."}, status=status.HTTP_404_NOT_FOUND)
    
    # request.FILES에서 파일을 가져오기
    picture = request.FILES.get('picture')

    # PictureSerializer 사용
    serializer = PictureSerializer(data={
        'picture': picture,
        'user': request.user.id,
        'bin': bin_instance.id
    })

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_info(request, pk):
    try:
        bin = Bin.objects.get(pk=pk)
    except Bin.DoesNotExist:
        return Response({'error': 'Bin not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()
    data['bin'] = bin.id
    data['user'] = request.user.id
    serializer = InformationSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)