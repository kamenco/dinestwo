from django.shortcuts import render

# Create your views here.

def menu(request):
    return render(request, 'menu/menu.html')  # Create menu.html template in menu/templates/menu/

def update_menu(request):
    # Logic for updating the menu goes here
    return render(request, 'menu/update_menu.html')  # Use your actual template
