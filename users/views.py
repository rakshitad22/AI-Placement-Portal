from django.shortcuts import render, redirect
from .models import UserProfile

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        UserProfile.objects.create(
            name=name,
            email=email,
            password=password
        )

        return redirect('/login/')

    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')