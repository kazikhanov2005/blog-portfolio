from .views import *
from django.urls import path


urlpatterns = [
    path('', blog_main, name='home'),
    path('blog/<int:blog_id>/', blog_detail, name='blog-detail'),
    path('blog/blog-list', blog_list, name='blog-list'),
     path('portfolio', portfolio, name='portfolio'),
    # path('blog/survey/', blog_survey, name='blog-survey'),

]
