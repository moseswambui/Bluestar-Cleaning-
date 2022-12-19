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

class CategoryAdminInline(admin.TabularInline):
    model = ServiceCategory
    list_display = ('name', 'price', 'type')
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "form")
    inlines = [CategoryAdminInline]

class ServiceVariationAdminInlines(admin.TabularInline):
    model = ServiceVariation
    list_display = ('category', 'variation_category', 'variation_value',)

class TechnicianVariationAdminInlines(admin.TabularInline):
    model = TechnicianVariation
    list_display = ('category', 'variation_category', 'variation_value',)

class ExtraServiceAdminInline(admin.TabularInline):
    model = ExtraServiceInfo
    list_display = ('name', 'description', 'category','unit_charges')
    
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "code",'price')
    list_editable = ('price',)
    inlines = [ExtraServiceAdminInline]
    list_filter = (
        'name',
    )
class ExtraServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category','unit_charges')
    list_editable = ('unit_charges')
class ServiceApplicationAdmin(admin.ModelAdmin):
    list_display = ("submission_number", "type", "category")

class AppointmentOrderAdmin(admin.ModelAdmin):
    list_display = ('category', 'service', 'appointment_date')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'type', 'category', 'consultant')

admin.site.register(FormField, FormFieldAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(FormSection, FormSectionAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
#admin.site.register(ServiceApplications, ServiceApplicationAdmin)
admin.site.register(AppointmentOrder, AppointmentOrderAdmin)
admin.site.register(Service)
admin.site.register(Consultant)
admin.site.register(ExtraServiceInfo)