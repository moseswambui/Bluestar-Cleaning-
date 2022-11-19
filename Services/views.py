from django.shortcuts import render
from .forms import AppointmentOrderForm,ServiceForm
from . models import *

def Index(request):
    type = ServiceType.objects.all()
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
        'type':type
    }

    return render(request, 'index.html', context)

def Myform(request):
    form = ServiceForm

    context = {
        'form':form
    }
    return render(request, 'forms.html', context)

def load_categorties(request):
    type_id = request.GET.get('service_type.id')
    categories = ServiceCategory.objects.filter(
        type_id = type_id
        ).order_by('name')

    context = {
        'categories':categories
    }
    return render(request, 'service_dropdown_list.html', context)


