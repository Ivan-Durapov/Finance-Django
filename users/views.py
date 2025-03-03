from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserLoginForm, UserRegisterForm
from .models import User


class HomeView(TemplateView):
    template_name = "index.html"

class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy("home")


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("home")



