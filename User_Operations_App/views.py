from django.shortcuts import render, redirect
from .models import Bureau, Personals
from django.core.files.storage import default_storage

def register(request):
    bureaus = Bureau.objects.all()
    if request.method == 'POST':
        # User registration
        if 'bureau' in request.POST:
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            bureau_id = request.POST.get('bureau')
            bureau = Bureau.objects.get(id=bureau_id)
            Personals.objects.create(
                name=name,
                surname=surname,
                email=email,
                password=password,
                bureau=bureau
            )
            return redirect('register')
        # Bureau registration
        elif 'bureau_name' in request.POST:
            from .models import Customer_of_Bureau
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            bureau_name = request.POST.get('bureau_name')
            personal_limit = request.POST.get('personal_limit')
            logo = request.FILES.get('bureau_logo')
            # Create representative personal
            personal = Personals.objects.create(
                name=name,
                surname=surname,
                email=email,
                password=password,
                status=True
            )
            bureau = Bureau.objects.create(
                name=bureau_name,
                logo=logo,
                personal_limit=personal_limit,
                representative=personal,
                status=True
            )
            return redirect('register')
    return render(request, 'register.html', {'bureaus': bureaus})