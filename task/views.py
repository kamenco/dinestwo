from django.shortcuts import render

# Create your views here.

def tasks(request):
    return render(request, 'tasks/tasks.html')  # Create menu.html template in menu/templates/menu/

def add_task(request):
    return render(request, 'tasks/add_task.html')


def update_task(request):
    return render(request, 'tasks/update_task.html')