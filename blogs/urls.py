from django.urls import path 
from blogs.views import *

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>', detail, name='detail'),
    path('add/', PostCreateView.as_view(), name="add"),
    path('<slug:slug>/comments/', comments, name='comments'),
]