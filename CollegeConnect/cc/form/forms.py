from django import forms
from cc.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class CCForm(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields = ['first_name', 'last_name', 'major', 'interest']

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Ex: "John"')
	last_name = forms.CharField(max_length=30, required=True, help_text='Ex: "Doe"')
	email = forms.EmailField(max_length=254, required=True, help_text='Ex: "jdoe@realuniversity.edu"')
	major = forms.CharField(max_length=30, required=True, help_text='Ex: "BS Computer Science"')
	interest = forms.CharField(required=False, help_text='Ex: "I love hiking, swimming, and programming!"')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'major', 'interest')
