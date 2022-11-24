from django.shortcuts import render
from .forms import AppointmentOrderForm,ServiceForm
from . models import *
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

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
    
    context = {
        'form':form,
        'types':types
    }

    return render(request, 'index.html', context)
class AppointmentListView(ListView):
    model = Service
    context_object_name = 'service'
class AppointmentCreateView(CreateView):
    model = Service
    #template_name = "index.html"
    form_class = ServiceForm
    success_url = reverse_lazy('appointment')

def load_categories(request):
    type_id = request.GET.get('type')
    print(type_id)
    categories = ServiceCategory.objects.filter(type_id=type_id).order_by('name')
    print(categories)
    context = {
        'categories':categories
    }
    return render(request, "Services/category_dropdown_list.html", context)

def load_consultants(request):
    consultant_id = request.GET.get("consultant")
    consultants = Consultant.objects.filter(consultant_id=consultant_id).order_by("name")
    context = {
        'consultants':consultants
    }
    return render(request, "consultant_dropdown_list.html", context)

def get_data(request):
    types = ServiceType.objects.all()
    categories = ServiceCategory.objects.all()

    context = {
        'types':types,
        'categories':categories
    }
    return render(request, 'index.html')




