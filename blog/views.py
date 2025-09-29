from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def blog_main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Главная страница</h1>")


def blog_detail(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Отдельный блог </h1>")


def blog_users(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Пользователи сайта</h1>")


def blog_survey(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Опрос </h1>")