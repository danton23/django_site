from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
       
       return render(request, "posts/index.html")
# Create your views here.
def test(request):
    allposts=Post.objects.all()
    limit=3
    return render(request, "posts/test.html",{"allposts":allposts, "limit":limit})
