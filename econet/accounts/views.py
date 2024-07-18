# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth import authenticate, update_session_auth_hash, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def profile(request):
    # 프로필 창(마이페이지)의 view 함수
    return render(request, 'accounts/account_delete.html')

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

@login_required
def account_setting(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        messages.success(request, 'Account settings updated successfully.')
        return redirect('profile')
    return render(request, 'accounts/account_setting.html')

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {'form': form})

# 이메일 변경 뷰
@login_required
def email_change(request):
    if request.method == 'POST':
        new_email = request.POST['email']
        request.user.email = new_email
        request.user.save()
        messages.success(request, 'Email updated successfully.')
        return redirect('profile')
    return render(request, 'accounts/email_change.html')

# 계정삭제 뷰
@login_required
def account_delete(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('/')
    return render(request, 'accounts/account_delete.html')