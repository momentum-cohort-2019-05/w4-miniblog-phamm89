from django.shortcuts import render, redirect, get_object_or_404
from miniblog.models import Blog, Blogger, BlogReader, BlogComment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blog = Blog.objects.all().count()
    
    # The 'all()' is implied by default. 
    num_blogger = Blogger.objects.count()
    num_blogreader = BlogReader.objects.count()
    num_blogcomment = BlogComment.objects.count()

    context = {
        'num_blog': num_blog,
        'num_blogger': num_blogger,
        'num_blogreader': num_blogreader,
        'num_blogcomment': num_blogcomment,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

class BlogReaderListView(LoginRequiredMixin, generic.ListView):
    model = BlogReader

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class BlogReaderDetailView(LoginRequiredMixin, generic.DetailView):
    model = BlogReader

    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    

