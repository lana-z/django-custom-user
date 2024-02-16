from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class HomeView(TemplateView):
    template_name = "home.html"

class LoginView(TemplateView):
    template_name = "registration/login.html"

class LogoutView(TemplateView):
    template_name = "home.html"
