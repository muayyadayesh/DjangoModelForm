from django import forms
from django.contrib.auth.models import User
from app.models import ProfileUserInfoModel

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username','email', 'password')


class ProfileUserInfoForm(forms.ModelForm):
    class Meta():
        model = ProfileUserInfoModel
        fields = ('portfoliowebsite', 'photo')
