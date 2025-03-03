from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input", "placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Пароль"}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input", "placeholder": "Email"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Пароль"}))
    password2 = forms.CharField(label="Підтвердіть пароль", widget=forms.PasswordInput(attrs={"class": "input", "placeholder": "Повторіть пароль"}))

    class Meta:
        model = User
        fields = ("email",)
