from django import forms

from .models import *
from django.urls import reverse_lazy
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
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email_address',
            'type',
            'category',
            'consultant',
            'service_date',
        )

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
        self.fields['type'].widget.attrs.update({
            'type':'service',
            'name':'category',
            'id':'category',
        })
        self.fields['category'].widget.attrs.update({
            'type':'select',
            'name':'service',
            'id':'service',
            
        })
        self.fields['consultant'].widget.attrs.update({
            'type':'select',
            'name':'consultant',
            'id':'consultant',
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

        self.fields['category'].queryset = ServiceCategory.objects.none()

        if "type" in self.data:
            try:
                type_id = int(self.data.get("type"))
                print(type_id)
                self.fields['category'].queryset = ServiceCategory.objects.filter(type_id=type_id).order_by('name')

            except (ValueError, TypeError):
                pass

        elif self.instance.id:
            self.fields['category'].queryset = self.instance.type.category_set.order_by('name')

        