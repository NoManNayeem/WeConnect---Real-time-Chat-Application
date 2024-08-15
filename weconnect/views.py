from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def home_page(request):
    return render(request, 'home_page.html')
