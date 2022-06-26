from django.shortcuts import render, redirect
from todo_app.models import TaskList
from todo_app.forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import os


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


@login_required
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
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            'message from ' + message_name,  # subject
            message,  # message
            message_email,  # from email
            [os.environ.get('EMAIL_HOST_USER')],  # to email
            fail_silently=False,
        )

        return render(request, 'todo_app/contact.html',
                      {'message_name': message_name})
    else:
        return render(request, 'todo_app/contact.html', {})


@login_required
def edit_task(request, task_id):

    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'todo_app/edit.html', {'task_obj': task_obj})


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Sorry but you can't do that!"))
    return redirect('todolist')


@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')


@login_required
def checkbox_done(request):
    if request.method == 'POST':
        task.update(done=False)
        done = request.POST.get('task_obj.done')


@login_required
def checkbox_important(request):
    if request.method == 'POST':
        task.update(important=False)
        important = request.POST.get('task_obj.important')
