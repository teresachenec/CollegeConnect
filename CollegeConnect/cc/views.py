from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, DeleteView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import auth
from cc.form.forms import SignUpForm

# Views related to user login
class LoginView(auth_views.LoginView):
	template_name = 'login.html'

	def login(request):
		if request.user.is_authencated():
			return redirect('admin')

		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = auth.authenticate(username=username, password=password)

			if user is not None:
				# correct username and password login the user
				auth.login(request, user)
				return redirect('admin_page')
			else:
				messages.error(request, 'Error wrong username/password')
		return render(request, 'blog/login.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			user.refresh_from_db()
			major = form.get('major')
			interst = form.get('interest')
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

class PasswordResetView(auth_views.PasswordResetView):
	template_name = 'password_reset.html'
	success_url = reverse_lazy('/login')

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
	template_name = 'password_reset_confirm.html'

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
	template_name = 'password_reset_complete.html'

class LogoutView(auth_views.LogoutView):
	template_name = 'logout.html'
	
	def logout(request):
		auth.logout(request)
		return render(request, 'logout.html')
	
	next_page = reverse_lazy('/login')

# Template views
class CCHomeView(TemplateView):
    template_name = "index.html"

class CCDetailView(DetailView):
    model = User
	# class CCCreateView(UpdateView):
	# model = User

class CCListView(ListView):
    model = User

class CCDeleteView(DeleteView):
    model = User
    #success_url = reverse_lazy('home_list')
