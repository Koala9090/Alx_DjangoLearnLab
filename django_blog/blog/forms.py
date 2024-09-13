from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['title', 'content']
        