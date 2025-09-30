from datetime import date
import requests
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



def get_location_by_ip():
    try:
        # Используем бесплатный API
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        if data['status'] == 'success':
            geo = f"📍{data['country']}, {data['city']}, {data['regionName']} "
            return geo
        else:
            print(None)

    except Exception as e:
        print(f"Ошибка: {e}")


def portfolio(request: HttpRequest) -> HttpResponse:
    birth_date = date(2005,7,13)
    today = date.today()
    age = (today - birth_date).days // 365
    name = 'Казиханов Шихсафар'
    geo = get_location_by_ip()
    context = {
        'age':age,
        'name': name,
        'geo': geo
    }

    return render(request, 'blog/portfolio.html', context)


def blog_list(request):
    posts = Post.objects.filter(status='published')
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def blog_survey(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Опрос </h1>")