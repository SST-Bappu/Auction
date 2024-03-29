from django.http import HttpResponse
from django.shortcuts import redirect
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff == True:
                return redirect('admin_dash')
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        group = None
        if request.user.is_staff == True:
            return view_func(request,*args,**kwargs)
        return redirect('home')
    return wrapper_function