from django.shortcuts import render, redirect
from .forms import MenuItemForm

# Create your views here.

def menu(request):
    return render(request, 'menu/menu.html')  # Create menu.html template in menu/templates/menu/

from django.shortcuts import render, redirect
from .forms import MenuItemForm

def update_menu(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirect to the menu page after submission
    else:
        form = MenuItemForm()
    context = {
        'form': form,
        'list': MenuItem.objects.all(),  # Pass the list of menu items for deletion
    }
    return render(request, 'menu/update_menu.html', context)


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirect to the menu page
    else:
        form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form': form})

