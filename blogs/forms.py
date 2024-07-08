from django.forms import ModelForm
from blogs.models import *

class BlogForm(ModelForm):
    class Meta:
        model = Post 
        fields = ['title', 'content']

class CommentForm(ModelForm):
    class Meta:
        model = Comment 
        fields = ['content']
