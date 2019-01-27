from django import forms
from cc.models import Profile

class CCForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'ratinlast_name', 'major', 'interest']