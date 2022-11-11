from django.shortcuts import render
from .forms import AppointmentOrderForm

def Index(request):
    print('In appointment Booking')
    if request.method == "POST":
        print('in post method')
        form = AppointmentOrderForm(request.POST)
        if form.is_valid():
            print('validating Form')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email_address = form.cleaned_data['email_address']

            print(first_name, email_address)

    else:
        form = AppointmentOrderForm

    context = {
        'form':form,
    }

    return render(request, 'index.html', context)
