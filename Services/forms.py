from django import forms

from .models import AppointmentOrder

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