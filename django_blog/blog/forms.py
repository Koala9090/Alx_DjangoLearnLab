from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['title', 'content','tags']
        widgets = {
            'tags': TagWidget(),  
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),}
    def cleam_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError('Comment must be at least 5 characters long')
        return content
