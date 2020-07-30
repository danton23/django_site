from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator


def index(request):
       
       return render(request, "posts/index.html")
# Create your views here.
def test(request):
    allposts=Post.objects.all()
    paginator=Paginator(allposts,2)    #2nd value is number of objects per page
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "posts/test.html",{"page_obj":page_obj})
def post(request, usename):
       use_post=Post.objects.get(post_title=usename)
       print(use_post)
       

       return render(request, "posts/post.html",{"use_post":use_post})
       
       
       
