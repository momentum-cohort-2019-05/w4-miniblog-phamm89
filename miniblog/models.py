from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique blog instances
from django.template.defaultfilters import truncatechars
from django.utils import timezone

# Models created here


class Blog(models.Model):
    """Model representing a blog, but not a specific entry of a blog."""
    blog_title = models.CharField(max_length=200)

    # Foreign Key used because blog can only have one blogger, but bloggers can have multiple blogs
    # Blogger as a string rather than object because it hasn't been declared yet in the file
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    
    # Blog Entry Date
    blog_entry_date = models.DateField(null=True, blank=True)

    # Blog post
    blog_entry = models.TextField(max_length=5000, help_text='Start your blog entry here', null=True)
    
    class Meta:
        ordering = ['-blog_entry_date']

    def __str__(self):
        """String for representing the Model object."""
        return self.blog_title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])


class Blogger(models.Model):
    """Model representing a blogger."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000, help_text='Tell us about yourself', null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular blog."""
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

class BlogReader(models.Model):
    """Model representing a blog reader."""
    user_name = models.CharField(max_length=100)
    profile_description = models.CharField(max_length=1000, help_text='Tell us about yourself', null=True)

    class Meta:
        ordering = ['user_name']

    def get_absolute_url(self):
        """Returns the url to access a particular blogger instance."""
        return reverse('blogreader-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.user_name}'


class BlogComment(models.Model):
    """Model for the blog comments that are attached to a specific blog entry"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for the comments.')
    blog_entry = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    user_name = models.ForeignKey('BlogReader', on_delete=models.SET_NULL, null=True)
    comment = models.TextField(max_length=200)
    comment_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        """String for representing the Model object."""
        return truncatechars(self.comment, 75)

    class Meta:
        ordering = ['comment_date']
    
    def get_absolute_url(self):
        """Returns the url to access a particular blogger instance."""
        return reverse('create', args=[str(self.id)])
    
    