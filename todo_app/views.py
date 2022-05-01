from django.shortcuts import render

# Create your views here.

def todolist(request):
    context = {
        'welcome_text': 'Welcome to Task Mate',
        }
    return render(request, 'todo_app/todo.html', context )


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