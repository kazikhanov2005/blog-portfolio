from datetime import date
import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Post, Category

def main(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(status='published')

    context = {
        'posts': posts,
    }
    return render(request, 'base.html', context)


def blog_main(self, request: HttpRequest) -> HttpResponse:
    title = 'Казиханов Шихсафар | Проекты'
    return render(request, 'blog/blog.html', locals())


def blog_detail(request: HttpRequest, blog_id) -> HttpResponse:
    post = get_object_or_404(Post, id=blog_id)
    context = {
        'post': post
    }
    return render(request, 'blog/blog_detail.html', context)


def projects(request: HttpRequest) -> HttpResponse:
    title = 'Казиханов Шихсафар | Проекты'

    return render(request, 'blog/projects.html', locals())










