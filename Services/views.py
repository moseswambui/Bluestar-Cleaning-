from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import AppointmentOrderForm,ServiceForm
from . models import *
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def Index(request):
    today = date.today()
    print(today)
    if request.method == "POST":
        print('request is post')
        form = ServiceForm(request.POST)
        if form.is_valid():
            print('form is valid')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email_address = form.cleaned_data['email_address']
            type = form.cleaned_data['type']
            category = form.cleaned_data['category']
            consultant = form.cleaned_data['consultant']
            service_date_string = form.cleaned_data['service_date_string']
            message = form.cleaned_data['message']
            
            print(service_date_string)
            service_details =Service.objects.create(
                first_name = first_name,
                last_name = last_name,
                phone_number = phone_number,
                email_address = email_address,
                type = type,
                service_date_string = service_date_string,
                category = category,
                consultant = consultant,
               
                message = message
            )
            service_details.save()

            ### Django Send Receipt Email
            subject = "Bluestar Order Confirmation"
            message = f'Hello {first_name}. Your Order on Date- {today}  for Service - {type.name} Category- {category.name} Has Been Confirmed. Our employee - {consultant} Will Fulfill your Order on the Appointed Date - {service_date_string}. Thank You!'
            email_from = settings.EMAIL_HOST_USER
            recipient = [email_address,]
            send_mail(subject, message, email_from, recipient_list=recipient)
            
            print ("form is saved")
            return redirect('index')
        else:
            print('form is not valid')
            print(form.errors)
    else:
        form = ServiceForm
    #if is_ajax(request):
        #print("ajax request")
        #if form.is_valid():
            #print(" form is valid ")
            #form.save()

        #else:
            #print('form is not valid')
            #print(form.errors)
    

    context = {
        'form':form,
        'today':today,
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
    type_id = request.GET.get("type")
    consultants = Consultant.objects.filter(type_id=type_id).order_by("name")
    print(consultants)
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

def load_category_image(request):
    category_id = request.GET.get("service")
    image= ExtraServiceInfo.objects.filter(category_id=category_id).order_by("name")
    print(image)
    for serv in image:
        print(serv.category.image)
    context = {
        'image':image
    }
    return render(request, "category_image.html", context) 



