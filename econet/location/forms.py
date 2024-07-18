from django import forms
from .models import CollectionBin

class CollectionBinForm(forms.ModelForm):
    class Meta:
        model = CollectionBin
        fields = ['user_location', 'photo', 'description', 'acceptable_items', 'unacceptable_items']
        labels = {
            'user_location': '사용자의 위치정보',
            'photo': '수거함의 사진',
            'description': '수거함의 위치 설명',
            'acceptable_items': '수거 대상 품목',
            'unacceptable_items': '수거 불가 품목',
        }
        widgets = {
            'user_location': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'acceptable_items': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'unacceptable_items': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
