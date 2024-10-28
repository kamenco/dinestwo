
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tasks(request):
    all_tasks = Task.objects.all()
    return render(request, 'task/tasks.html', {'tasks': all_tasks})
  # Create menu.html template in menu/templates/menu/

@login_required
def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        due_date = request.POST.get('due_date')
        is_urgent = request.POST.get('is_urgent') == 'on'

        Task.objects.create(
            task_name=task_name,
            task_description=task_description,
            due_date=due_date,
            is_urgent=is_urgent
        )
        return redirect('tasks')  # Redirect to the tasks list after adding a task

    return render(request, 'task/add_task.html')

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.task_name = request.POST.get('task_name')
        task.task_description = request.POST.get('task_description')
        task.due_date = request.POST.get('due_date')
        task.is_urgent = request.POST.get('is_urgent') == 'on'
        task.save()
        return redirect('tasks')  # Redirect to the tasks list after updating a task

    return render(request, 'task/update_task.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')


