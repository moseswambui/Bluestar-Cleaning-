from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey

class FormField(models.Model):
    key = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="")
    min = models.PositiveSmallIntegerField(blank=True, null=True)
    max = models.PositiveSmallIntegerField(blank=True, null=True)
    min_date = models.DateTimeField(blank=True, null=True)
    max_date = models.DateTimeField(blank=True, null=True)
    slug = None

    class Meta:
        ordering = ("name",)
        verbose_name = _("Form Field")
        verbose_name_plural = _("Form Fields")

class Form(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="")
    slug = None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Form")
        verbose_name_plural = _("Forms")


class FormSection(models.Model):
    index = models.PositiveSmallIntegerField()
    key = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="")
    form = models.ForeignKey(Form, related_name="sections", on_delete=models.PROTECT)
    fields = models.ManyToManyField(to=FormField, through="FormSectionField")
    slug = None

    class Meta:
        ordering = (
            "index",
            
        )
        verbose_name = _("Form Section")
        verbose_name_plural = _("Form Sections")

    def __str__(self):
        return f"{self.name} - {self.form.name}"

class FormSectionField(models.Model):
    index = models.PositiveSmallIntegerField( null=True, blank=True)
    field = models.ForeignKey(FormField, on_delete=models.PROTECT)
    section = models.ForeignKey(FormSection, on_delete=models.PROTECT)
    hidden = models.BooleanField(default=False)
    default = models.CharField(max_length=50, null=True, blank=True)
    readonly = models.BooleanField( null=True, blank=True)
    is_required = models.BooleanField(default=False)
    slug = None

    class Meta:
        ordering = (
            "index",
        )
        verbose_name = _("Form Section Field")
        verbose_name_plural = _("Form Section Fields")

    def __str__(self):
        return f"{self.field.name} - {self.section.name}"

class ServiceType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="")
    code = models.CharField(max_length=100, default="")
    form = models.ForeignKey(Form,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="")
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    code = models.CharField(max_length=100, default="")
    type = models.ForeignKey(ServiceType,blank=True, null=True, related_name="categories", on_delete=models.PROTECT)
    slug = None

    class Meta:
        ordering = ("name",)
        verbose_name = _("Service Category")
        verbose_name_plural = _("Service Categories")

    def __str__(self):
        return self.name

class Consultant(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey(ServiceType,blank=True, null=True, related_name="consultants", on_delete=models.PROTECT)
    slug = None

    class Meta:
        ordering = ("name",)
        verbose_name = _("Consultant")
        verbose_name_plural = _("Consultants")

    def __str__(self):
        return self.name

class ExtraServiceInfo(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(ServiceCategory, null=True, blank=True, on_delete=models.CASCADE)
    unit_charges = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

PAYMENT_CHOICES = (
    ('Pay During Visit', 'Pay during Visit'),
)
class Service(models.Model):  
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    type= models.ForeignKey(ServiceType, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(
        ServiceCategory,
        null=True,
        blank = True,
        on_delete=models.CASCADE,
        )
    consultant = models.ForeignKey(
        Consultant,
        on_delete = models.CASCADE,
        null=True,
        blank=True,
        )
    service_date = models.DateField(auto_now_add=True, blank=True, null=True)

    cleaning_date = models.DateTimeField(blank=True, null=True)
    serviceinfo = models.ForeignKey(
        ExtraServiceInfo,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    message = models.TextField(null=True, blank=True)
    pay = models.CharField(max_length=200, default="Pay During Visit")

    def __str__(self):
        return str(self.category)

class ServiceVariationManager(models.Manager):
    def service(self):
        return super(ServiceVariationManager, self).filter(variation_category="service")
    def charges(self):
        return super(ServiceVariationManager, self).filter(variation_category="charges")

variation_category_choice=(
    ('service','service'),
    ('charges','charges'),
   
)
class ServiceVariation(models.Model):
    category = models.ForeignKey(ServiceCategory, null=True, blank=True, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now=True)

    objects = ServiceVariationManager()
    class Meta:
        verbose_name = ("Service Variation")
        verbose_name_plural =("Service Variations")

    def __str__(self):
        return self.variation_value

class TechnicianVariationManager(models.Manager):
    def technician(self):
        return super(TechnicianVariationManager, self).filter(variation_category="technician")
   
variation_technician_choice=(
    ('technician','technician'),
   
)
class TechnicianVariation(models.Model):
    category = models.ForeignKey(ServiceCategory, null=True, blank=True, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_technician_choice)
    variation_value = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now=True)

    objects = TechnicianVariationManager()
    class Meta:
        verbose_name = ("Technician Variation")
        verbose_name_plural =("Technician Variations")

    def __str__(self):
        return self.variation_value

class AppointmentOrder(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    category = models.CharField(max_length=250, null=True, blank=True)
    service = models.CharField(max_length=250, null=True, blank=True)
    consultant = models.CharField(max_length=250, null=True, blank=True)
    appointment_date = models.DateTimeField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    payment_mode = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.category_name
        
    class Meta:
        verbose_name = _("Appointment")
        verbose_name_plural = _("Appointments")


