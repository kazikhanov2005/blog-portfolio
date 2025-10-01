from .views import *
from django.urls import path


urlpatterns = [
    path('', main, name='home'),
    path('blog/', blog_main, name='blog'),
    path('projects/', projects, name='projects'),
    # path('blog/<int:blog_id>/', blog_detail, name='blog-detail'),

    # path('blog/survey/', blog_survey, name='blog-survey'),

]
