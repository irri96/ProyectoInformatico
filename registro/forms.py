from django import forms
from django.contrib.auth.forms import UserCreationForm
from Core.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='')
    last_name = forms.CharField(max_length=30, required=True, help_text='')
    rut = forms.CharField(max_length=30, required=True, help_text='')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'rut')