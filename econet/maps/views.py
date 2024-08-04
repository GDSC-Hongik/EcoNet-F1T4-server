from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Bin, MapoDistrict
from .serializers import BinSerializer, MapoDistrictSerializer, BinDetailSerializer

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
