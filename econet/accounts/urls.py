from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup),
#    path('', )  마이페이지(프로필창)
    path('login/', auth_views.LoginView.as_view(template_name = "accounts/login.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(next_page=""), name = "logout"),
]