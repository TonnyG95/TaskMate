from django.shortcuts import render
from todo_app.models import TaskList

# Create your views here.

def todolist(request):

    all_tasks = TaskList.objects.all

    return render(request, 'todo_app/todo.html', {'all_tasks':all_tasks})


def about(request):
    context = {
        'about_text': 'About us',
        }
    return render(request, 'todo_app/about.html', context )

def contact(request):
    context = {
        'contact_text': 'Contact us',
        }
    return render(request, 'todo_app/contact.html', context )