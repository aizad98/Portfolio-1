from django.shortcuts import render
from .models import Education

def education_list(request):
    qualifications = Education.objects.all().order_by('-start_year')
    return render(request, 'education/education_list.html', {'qualifications': qualifications})