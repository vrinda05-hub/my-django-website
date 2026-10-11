from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            Task.objects.create(
                title=title,
                description=description
            )
            return redirect('home')

    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'tasks': tasks})


def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()

    return redirect('home')


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()

    return redirect('home')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')