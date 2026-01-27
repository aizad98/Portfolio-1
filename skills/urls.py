from django.urls import path
from . import views

urlpatterns = [
    # This empty string means 'the root of the skills app'
    path('', views.skills_view, name='skills_list'),
]