import requests
from django.http import JsonResponse
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Bin, MapoDistrict
from .serializers import BinSerializer, MapoDistrictSerializer, BinDetailSerializer, PictureSerializer, InformationSerializer

def naver_map_data(request):
    query = request.GET.get('query', '서울 마포구')  # 'query' 파라미터를 받아옴, 기본값은 '서울 마포구'
    url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'

    headers = {
        'X-NCP-APIGW-API-KEY-ID': settings.NAVER_MAPS_CLIENT_ID,
        'X-NCP-APIGW-API-KEY': settings.NAVER_MAPS_CLIENT_SECRET,
    }
    
    params = {
        'query': query  # 검색할 위치 정보
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return JsonResponse(response.json())  # 성공 시 API 응답을 반환
    else:
        return JsonResponse({'error': 'Failed to fetch data from Naver Maps API'}, status=response.status_code)  # 실패 시 에러 메시지 반환


@api_view(['GET'])
@permission_classes([AllowAny])
def bin_list(request):
    if request.method == 'GET':
        category = request.GET.get('category', None)  # URL 쿼리 파라미터에서 'category'를 가져옴
        if category:
            bins = Bin.objects.filter(category=category)  # category에 따라 필터링
        else:
            bins = Bin.objects.all()  # 모든 배출함 데이터 가져오기
        bin_serializer = BinSerializer(bins, many=True)  
        return Response({"bins": bin_serializer.data})


@api_view(['GET'])
@permission_classes([AllowAny])
def district_list(request):
    if request.method == 'GET':
        mapo_districts = MapoDistrict.objects.all()  # 모든 마포구역 데이터 가져오기
        mapo_district_serializer = MapoDistrictSerializer(mapo_districts, many=True)  
        return Response({"mapo_districts": mapo_district_serializer.data})


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