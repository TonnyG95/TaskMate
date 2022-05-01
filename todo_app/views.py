from django.shortcuts import render, redirect
from todo_app.models import TaskList
from todo_app.forms import TaskForm
from django.contrib import messages

# Create your views here.


def todolist(request):

    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New task added!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all
        return render(request, 'todo_app/todo.html', {'all_tasks': all_tasks})


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')


def about(request):
    context = {
        'about_text': 'About us',
    }
    return render(request, 'todo_app/about.html', context)


def contact(request):
    context = {
        'contact_text': 'Contact us',
    }
    return render(request, 'todo_app/contact.html', context)
