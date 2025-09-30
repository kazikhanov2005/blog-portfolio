from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Post, Category


def blog_main(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/blog_main.html', context={'posts':posts})


def blog_detail(request: HttpRequest, blog_id) -> HttpResponse:
    post = get_object_or_404(Post, id=blog_id)
    context = {
        'post': post
    }
    return render(request, 'blog/blog_detail.html', context)


def blog_users(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Пользователи сайта</h1>")


def blog_list(request):
    posts = Post.objects.filter(status='published')
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def blog_survey(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Опрос </h1>")