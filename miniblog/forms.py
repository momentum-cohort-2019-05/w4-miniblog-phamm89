from django.db import models
from django.forms import ModelForm
from miniblog.models import Blog, Blogger, BlogReader, BlogComment

class BlogCommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ['blog_entry', 'user_name', 'comment', 'comment_date']
    