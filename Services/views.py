from django.shortcuts import render
from django.http import JsonResponse
from .forms import AppointmentOrderForm,ServiceForm
from . models import *
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

def Index(request):
    form = ServiceForm()
   
    
    context = {
        'form':form,
        
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

def load_extra_info(request):
    category_id = request.GET.get("service")
    serviceinfo = ExtraServiceInfo.objects.filter(category_id=category_id).order_by("name")
    print(serviceinfo)
    for serv in serviceinfo:
        print(serv.name)
    context = {
        'serviceinfo':serviceinfo
    }
    return render(request, "extra_fields_category.html", context)

def load_pricing(request):
    category_id = request.GET.get("service")
    pricing = ExtraServiceInfo.objects.filter(category_id=category_id).order_by("name")
    print(pricing)
    for serv in pricing:
        print(serv.name)
    context = {
        'pricing':pricing
    }
    return render(request, "extra_fields_pricing.html", context)

def load_name(request):
    category_id = request.GET.get("service")
    name = ExtraServiceInfo.objects.filter(category_id=category_id).order_by("name")
    print(name)
    for serv in name:
        print(serv.name)
    context = {
        'name':name
    }
    return render(request, "extra_fields_name.html", context)


