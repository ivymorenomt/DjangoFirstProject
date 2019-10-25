from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#to register a user
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	#gives a configuration in one space. form save will save it to this model
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

#to update a user
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	#gives a configuration in one space. form save will save it to this model
	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']