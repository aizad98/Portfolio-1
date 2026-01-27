from django.shortcuts import render
from .models import HeroSection

def home_view(request):
    hero = HeroSection.objects.first() # Gets the first entry from Admin
    return render(request, 'main/home.html', {'hero': hero})