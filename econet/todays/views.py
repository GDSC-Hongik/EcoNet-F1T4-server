from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import District
from .serializers import DistrictSerializer

class DistrictListView(APIView):
    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)
