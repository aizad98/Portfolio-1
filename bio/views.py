from django.shortcuts import render
from bio.models import Bio

def home(request):
    # Fetching only the first entry to show on the portfolio
    bio_data = Bio.objects.first()
    return render(request, 'index.html', {'bio': bio_data})