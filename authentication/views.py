from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.forms import BaseModelForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from authentication.decorators import *
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import auth

# Create your views here.
@method_decorator(redirectAuthenticatedUser, name='dispatch')
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.form = form
        response = super().form_valid(form)
        return response
    
    def get_success_url(self) -> str:
        user = self.onsucces(self.form)
        return reverse_lazy('/')
    
    def onsucces(self, form: BaseModelForm):
       
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = auth.authenticate(username=username, password = password)
        auth.login(self.request, user)
        return user