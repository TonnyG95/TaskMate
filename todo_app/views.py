from django.shortcuts import render, redirect
from todo_app.models import TaskList
from todo_app.forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):

    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save()
        messages.success(request, ("New task added!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(owner=request.user)

      


        return render(request, 'todo_app/todo.html', {'all_tasks': all_tasks})


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
         messages.error(request, ("Sorry, you can't do that!"))
        
    return redirect('todolist')


def about(request):
    context = {
        'about_text': 'About us',
    }
    return render(request, 'todo_app/about.html', context)


def index(request):
    context = {
        'index_text': 'Homepage',
    }
    return render(request, 'todo_app/index.html', context)


def contact(request):
    context = {
        'contact_text': 'Contact us',
    }
    return render(request, 'todo_app/contact.html', context)


def edit_task(request, task_id):
     
     if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance= task)
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited!"))
        return redirect('todolist')
     else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'todo_app/edit.html', {'task_obj': task_obj})


def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True 
        task.save()
    else:
         messages.error(request, ("Sorry but you can't do that!"))
    return redirect('todolist')


def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False 
    task.save()
    return redirect('todolist')