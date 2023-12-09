from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfilInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Şifre"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"kullanıcı adı"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"E-posta"}))
    class Meta():
        model=User
        fields=["username","email","password"]


class UserProfilForm(forms.ModelForm):
    portfolio_site=forms.URLField(widget=forms.URLInput(attrs={"class":"form-control","placeholder":"Siten"}))
    class Meta():
        model=UserProfilInfo
        fields=["portfolio_site","profile_pic"]