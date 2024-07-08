from django.shortcuts import redirect, render
from django.http import HttpResponse

def redirectAuthenticatedUser(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profiles:profile', request.user.slug)
        else:
            return view_func(request, *args, **kwargs)
    return wrapper

def isSelf(view_func):
    def wrapper(request, *args, **kwargs):
       
        if request.user.slug == kwargs['slug']:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorised to access this page')
    return wrapper