from django.forms import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'last_name', 'first_name','image')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ( 'last_name', 'first_name','image')

