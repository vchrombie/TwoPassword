from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'email',
            'password1',
            'password2',
        )
