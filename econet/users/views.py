from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from users.serializers import UserSerializer



@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    """
    email = request.data.get('email')
    nickname = request.data.get('nickname')
    password = request.data.get('password')
    

    serializer = UserSerializer(data=request.data)
    serializer.email = email
    serializer.nickname = nickname

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
"""

    serializer = UserSerializer(data=request.data)
    
    # 시리얼라이저의 유효성을 검사합니다.
    if serializer.is_valid():
        # 유효한 경우, 저장하여 사용자 객체를 생성합니다.
        user = serializer.save()
        
        # 비밀번호를 설정합니다.
        user.set_password(request.data.get('password'))
        user.save()
        
        # 응답을 반환합니다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 유효하지 않은 경우, 에러를 반환합니다.
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(email=email, password=password)
    if user is None:
        return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)

    return Response({'refresh_token': str(refresh),
                     'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)