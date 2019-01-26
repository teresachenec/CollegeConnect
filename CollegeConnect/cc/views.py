from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
class LoginView(auth_views.LoginView):
	template_name = 'login.html'

class PasswordResetView(auth_views.PasswordResetView):
	template_name = 'password_reset.html'
	success_url = reverse_lazy('/login')

class LogoutView(auth_views.LogoutView):
	template_name = 'logout.html'
	next_page = reverse_lazy('/login')

class CCHomeView(TemplateView):
    template_name = "index.html"

class CCDetailView(DetailView):
    model = User
	class CCCreateView(UpdateView):
	model = User

class CCListView(ListView):
    model = User

class CCDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('animal_list')

