from .views import *
from django.urls import path

urlpatterns = [
    path('', blog_main, name='blog-main'),
    path('blog/users/', blog_users, name='blog-users'),
    path('blog/detid/', blog_detail, name='blog-detail'),
    path('blog/survey/', blog_survey, name='blog-survey'),

]
