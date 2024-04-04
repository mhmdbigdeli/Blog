#https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , Http404
from .models import Post
# Create your views here.
#https://docs.djangoproject.com/en/5.0/topics/http/views/
def index(request):
    return HttpResponse("index")

def post_list(request):
    posts = Post.published.all()
    context = {
        'posts':posts
        }
    return render(request, "blog/list.html", context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    context = {
        'post':post
        }
    return render(request, "blog/detail.html", context)
