

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm  # Correct import for the form
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('home')  # Redirect to a home or dashboard page
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to the login page or any page you want after logout



def user_registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('home')  # Redirect to a home or dashboard page
        else:
            messages.error(request, "Error in registration. Please correct the errors below.")
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/registration.html', {'form': form})

# Redirect users based on their role

@login_required
def dashboard_redirect(request):
    from django.urls import reverse  # Avoid circular imports
    if request.user.is_superuser:
        return redirect(reverse('update_menu'))
    else:
        return redirect(reverse('customer_dashboard'))
