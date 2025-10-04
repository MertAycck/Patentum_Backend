from django.shortcuts import render
from .models import Bureau

def register(request):
    bureaus = Bureau.objects.all()
    return render(request, 'register.html', {'bureaus': bureaus})