from django.shortcuts import render
from .forms import AppointmentOrderForm,ServiceForm
from . models import *

def Index(request):
    types = ServiceType.objects.all()
    form = ServiceForm()

    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            print('validating Form')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email_address = form.cleaned_data['email_address']

            print(first_name, email_address)

    else:
        form = ServiceForm
    print(type)
    context = {
        'form':form,
        'types':types
    }

    return render(request, 'index.html', context)

def Myform(request):
    form = ServiceForm

    context = {
        'form':form
    }
    return render(request, 'forms.html', context)




