import requests
from django.http import JsonResponse
from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import District
from .serializers import DistrictSerializer

class DistrictListView(APIView):
    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)

def naver_map(request):
    query = request.GET.get('query', '서울')  # 'query' 파라미터를 받아옴, 기본값은 '서울'
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
