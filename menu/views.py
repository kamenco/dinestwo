from django.shortcuts import render

# Create your views here.

def menu(request):
    return render(request, 'menu/menu.html')  # Create menu.html template in menu/templates/menu/
