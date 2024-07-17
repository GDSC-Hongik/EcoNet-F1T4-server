# Create your views here.
from django.shortcuts import render

# 회원가입
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                useremail=request.POST['useremail'],
                password=request.POST['password1'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'accounts/signup.html')
    return render(request, 'accounts/signup.html')

