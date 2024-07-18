from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('signup/', views.signup),
    path('login/', auth_views.LoginView.as_view(template_name = "accounts/login.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(next_page=""), name = "logout"),
    path('accountsetting/', views.account_setting, name='account-setting'),
    path('pwchange/', views.password_change, name='password-change'),
    path('emailchange/', views.email_change, name='email-change'),
    path('accountdelete/', views.account_delete, name='account-delete'),
]