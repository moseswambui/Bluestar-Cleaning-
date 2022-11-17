from django.contrib import admin

from .models import *

class FormFieldAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "key")
    search_fields = ("name",)

class FormSectionAdmin(admin.ModelAdmin):
    list_display = ("form", "name", "key", "description", "index")
    search_fields = (
        "key",
        "name",
    )

class FormAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    ordering = ("name",)

class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "form")

class ServiceVariationAdminInlines(admin.TabularInline):
    model = ServiceVariation
    list_display = ('category', 'variation_category', 'variation_value',)

class TechnicianVariationAdminInlines(admin.TabularInline):
    model = TechnicianVariation
    list_display = ('category', 'variation_category', 'variation_value',)

class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "code")
    inlines = [ServiceVariationAdminInlines, TechnicianVariationAdminInlines]
    list_filter = (
        'name',
    )

class ServiceApplicationAdmin(admin.ModelAdmin):
    list_display = ("submission_number", "type", "category")

class AppointmentOrderAdmin(admin.ModelAdmin):
    list_display = ('category', 'service', 'appointment_date')

admin.site.register(FormField, FormFieldAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(FormSection, FormSectionAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
#admin.site.register(ServiceApplications, ServiceApplicationAdmin)
admin.site.register(AppointmentOrder, AppointmentOrderAdmin)
admin.site.register(Service)
admin.site.register(Consultant)