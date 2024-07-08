from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from authentication.views import *

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register')
]