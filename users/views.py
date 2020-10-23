
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'users/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('blog-home')
        else:
            return render(request, 'users/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'users/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('blog-home')
        else:
            return render(request, 'users/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'users/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog-home')