from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # here we have to write the todo list name to get to the right link

]