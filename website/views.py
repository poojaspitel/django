from django.shortcuts import render
from .models import Contact


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            phone=phone
        )

    return render(request, 'contact.html')