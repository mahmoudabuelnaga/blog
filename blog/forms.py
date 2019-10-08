from django import forms
from .models import Post

class PostcreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')