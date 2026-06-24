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
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserProfile.objects.get(
                email=email,
                password=password
            )

            return render(request, 'dashboard.html')

        except UserProfile.DoesNotExist:
            return render(request, 'login.html', {
                'error': 'Invalid Email or Password'
            })

    return render(request, 'login.html')