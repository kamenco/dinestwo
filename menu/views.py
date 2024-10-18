from django.shortcuts import render, redirect
from .forms import MenuItemForm
from .models import MenuItem
from django.shortcuts import get_object_or_404


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
  

def update_menu(request):
    if request.method == 'POST':
        # Check if the add button was clicked
        if 'add' in request.POST:
            form = MenuItemForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('menu')  # Redirect to the menu page after submission

        # Check if the delete button was clicked
        elif 'delete' in request.POST:
            recipe_id = request.POST.get('recipe_id')  # Get the recipe ID from the form
            if recipe_id:
                try:
                    recipe = MenuItem.objects.get(id=recipe_id)  # Find the recipe by ID
                    recipe.delete()
                    return redirect('update_menu')
                except MenuItem.DoesNotExist:
                    context = {
                        'form': MenuItemForm(),
                        'list': MenuItem.objects.all(),
                        'error_message': 'Recipe not found.'
                    }
                    return render(request, 'menu/update_menu.html', context)

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

    

def menu_item_detail(request, item_id):
    recipe = get_object_or_404(MenuItem, id=item_id)
    context = {
        'recipe': recipe,
        'page_title': recipe.name,
    }
    return render(request, 'menu/menu_item_detail.html', context)
