from django.shortcuts import render
from .models import Skill

def skills_view(request):
    # Fetch all skill objects from the database
    all_skills = Skill.objects.all()
    return render(request, 'skills/skills_list.html', {'skills': all_skills})