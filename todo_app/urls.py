
from django.urls import path
from . import views 

urlpatterns = [
    path('tasks/', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
