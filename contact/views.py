from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'contact/contact.html')  # Create menu.html template in menu/templates/menu/
