from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Admin Login


def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            auth.login(request, user)
            return redirect('/backend/dashboard')

        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'backend/login.html')
    else:
        return render(request, 'backend/login.html')


# Admin Dashboard
def dashboard(request):
    return render(request, 'backend/dashboard.html')
