from .views import *
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', blog_main, name='blog-main'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('blog/blog-list', blog_list, name='blog-list')
    # path('blog/detid/', blog_detail, name='blog-detail'),
    # path('blog/survey/', blog_survey, name='blog-survey'),

]
