from django import forms

from .models import *

class AppointmentOrderForm(forms.ModelForm):
    class Meta:
        model = AppointmentOrder
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email_address',
            'category',
            'service',
            'consultant',
            'appointment_date',
            'message',
            'payment_mode',
           
        ]

    def __init__(self, *args, **kwargs):
        super(AppointmentOrderForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'type':'text',
            'name':'fname',
            'id':'fname',
            'class':'form-control',
            'placeholder':'First Name',
        })

        self.fields['last_name'].widget.attrs.update({
            'type':'text',
            'name':'lname',
            'id':'lname',
            'class':'form-control',
            'placeholder':'Last Name',
        })

        self.fields['phone_number'].widget.attrs.update({
            'type':'text',
            'name':'pnumber',
            'id':'pnumber',
            'class':'form-control',
            'placeholder':'Contact: 0717828930',
        })

        self.fields['email_address'].widget.attrs.update({
            'type':'email',
            'name':'email',
            'id':'email',
            'class':'form-control',
            'placeholder':'Your E-Mail Address',
        })

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email_address',
            'service_type',
            'service_category',
            'consultant',
            'service_date',
           
           
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'type':'text',
            'name':'fname',
            'id':'fname',
            'class':'form-control',
            'placeholder':'First Name',
        })

        self.fields['last_name'].widget.attrs.update({
            'type':'text',
            'name':'lname',
            'id':'lname',
            'class':'form-control',
            'placeholder':'Last Name',
        })

        self.fields['phone_number'].widget.attrs.update({
            'type':'text',
            'name':'pnumber',
            'id':'pnumber',
            'class':'form-control',
            'placeholder':'Contact: 0717828930',
        })

        self.fields['email_address'].widget.attrs.update({
            'type':'email',
            'name':'email',
            'id':'email',
            'class':'form-control',
            'placeholder':'Your E-Mail Address',
        })
        self.fields['service_type'].widget.attrs.update({
            'type':'email',
            'name':'category',
            'id':'category',
        })
        self.fields['service_category'].widget.attrs.update({
            'type':'select',
            'name':'service',
            'id':'service',
        })
        self.fields['service_date'].widget.attrs.update({
            'type':'text',
            'name':'dp',
            'id':'dp',
            'class':'datepicker-here form-control',
            'placeholder':'Select Multiple Dates',
        })
        self.fields['service_date'].widget.attrs.update({
            'type':'text',
            'name':'dp',
            'id':'dp',
            'class':'datepicker-here form-control',
            'placeholder':'Select Multiple Dates',
        })

        self.fields['service_category'].queryset = ServiceCategory.objects.none()

        if 'service_type' in self.data:
            try:
                service_type_id = int(self.data.get('service_type'))
                self.fields['service_category'].queryset = ServiceCategory.objects.filter(service_type_id=service_type_id).order_by('name')

            except(ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields['service_category'].queryset = self.instance.service_type.service_category_set.order_by('name')
             
