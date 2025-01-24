from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home/index.html')

# Provide content tailored for customers without admin-related links.

def customer_dashboard(request):
    return render(request, 'home/customer_dashboard.html')
