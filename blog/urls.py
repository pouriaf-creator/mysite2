
from django.urls import path
from blog.views import *
from .views import blog_view, blog_single, test_page, test


app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='index'),
    path('test',test_page,name='test_page'),
    path('<int:pid>',blog_single,name='single'),
    path('post-<int:pid>',test,name='test'),
]