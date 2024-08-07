from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from .models import Password

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is not registered.")
        return email

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PasswordEntryForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['url', 'username', 'password', 'choice_text']
        widgets = {
            'password': forms.PasswordInput(),  # Use PasswordInput to hide the password characters
        }