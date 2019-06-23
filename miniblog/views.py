from django.shortcuts import render, redirect, get_object_or_404
from miniblog.models import Blog, BlogInstance, Blogger, BlogReader, BlogComment
from django.views import generic

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blog = Blog.objects.all().count()
    num_bloginstance = BlogInstance.objects.all().count()
    
    # The 'all()' is implied by default. 
    num_blogger = Blogger.objects.count()
    num_blogreader = BlogReader.objects.count()
    num_blogcomment = BlogComment.objects.count()

    context = {
        'num_blog': num_blog,
        'num_bloginstance': num_bloginstance,
        'num_blogger': num_blogger,
        'num_blogreader': num_blogreader,
        'num_blogcomment': num_blogcomment,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BlogInstanceListView(generic.ListView):
    model = BlogInstance
    paginate_by = 5

class BloggerListView(generic.ListView):
    model = Blogger
    

