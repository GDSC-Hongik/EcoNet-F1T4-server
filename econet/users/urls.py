from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from . import views

urlpatterns = [
    #로그인, 회원가입, 로그아웃    
    path('login/', views.login, name='login'),
    path('signup/',  views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('mypage/', views.user_profile, name='user_profile'),

    #토큰
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
