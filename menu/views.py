from django.shortcuts import render, redirect
from .forms import MenuItemForm
from .models import MenuItem
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

# Create menu.html template in menu/templates/menu/

def menu(request):
    category = request.GET.get('category')  # Get the category filter from the form
    if category:
        # Filter recipes based on the selected category
        recipes = MenuItem.objects.filter(category=category)
    else:
        # Fetch all recipes if no category is selected
        recipes = MenuItem.objects.all()

    context = {
        'list': recipes,  # Pass the list of recipes to the template
        'page_title': 'Menu',
    }
    return render(request, 'menu/menu.html', context)

@login_required
def update_menu(request):
    form = MenuItemForm()  # Initialize the form for adding new items

    if request.method == 'POST' and 'add' in request.POST:
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu item successfully added!")
            return redirect('menu')  # Redirect to the menu page after adding the item

    context = {
        'form': form,
        'list': MenuItem.objects.all(),  # Pass the list of menu items for deletion
    }
    return render(request, 'menu/update_menu.html', context)




@login_required
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirect to the menu page
    else:
        form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form': form})

    
@login_required
def menu_item_detail(request, item_id):
    recipe = get_object_or_404(MenuItem, id=item_id)
    context = {
        'recipe': recipe,
        'page_title': recipe.name,
    }
    return render(request, 'menu/menu_item_detail.html', context)

@login_required
def delete_menu_item(request, menu_item_id):
    
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    if request.method == 'POST':
        menu_item.delete()
        messages.success(request, "Menu item successfully deleted!")
        return redirect('update_menu')




