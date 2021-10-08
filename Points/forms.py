from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    username = forms.CharField(label="Username")
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'birth_date', 'password1', 'password2', )