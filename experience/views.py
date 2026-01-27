from django.shortcuts import render
from .models import Experience

def experience_list(request):
    # Fetching all experiences ordered by date
    exp_data = Experience.objects.all().order_by('-start_date')
    return render(request, 'experience/experience_list.html', {'experiences': exp_data})