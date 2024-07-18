from django import forms
from .models import User
from .models import Group

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'introduction', 'joined_groups', 'password', 'tier']
        # 사용자가 입력할 수 있는 필드 목록 지정
        widgets = {
            'joined_groups': forms.CheckboxSelectMultiple,
            'password': forms.PasswordInput,    # 비밀번호 입력을 받기 위한 위젯 옵션
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['board_id', 'name', 'introduction', 'chat_link', 'activity_scope', 'recruitment']
        # 사용자가 입력할 수 있는 필드 목록 지정
        widgets = {
            'introduction': forms.Textarea(attrs={'rows': 5}),  # Textarea 위젯: 여러 줄의 입력 가능
            'chat_link': forms.URLInput(attrs={'placeholder': 'https://'}), # URL 입력 받기 위한 위젯 옵션, https는 기본 세팅 - http는 무시?
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']