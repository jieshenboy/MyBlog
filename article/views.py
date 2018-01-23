from django.shortcuts import render
from django.http import  HttpResponse
from article.models import Article
from django.http import Http404
from datetime import datetime
# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id = str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoseNotExist :
        raise  Http404
    return  render(request, 'archives.html', {'post_list' : post_list,
                                              'error' : False})
def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})
