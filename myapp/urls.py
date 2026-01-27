from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='Todos'),
    # here we have to write the todo list name to get to the right link

]
