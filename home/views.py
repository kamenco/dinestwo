from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page(request):
    return render(request, 'home/index.html')

# Provide content tailored for customers without admin-related links.

# def customer_dashboard(request):
#    return render(request, 'home/customer_dashboard.html')

@login_required
def superuser_dashboard(request):
    return render(request, 'home/superuser_dashboard.html')

@login_required
def customer_dashboard(request):
    return render(request, 'home/customer_dashboard.html')

