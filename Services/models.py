from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    form = models.ForeignKey(Form, on_delete=models.CASCADE)




class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default="")
    code = models.CharField(max_length=100, default="")
    type = models.ForeignKey(ServiceType, related_name="categories", on_delete=models.PROTECT)
    slug = None

    class Meta:
        ordering = ("name",)
        verbose_name = _("Service Category")
        verbose_name_plural = _("Service Categories")

    def __str__(self):
        return self.name


class ServiceApplications(models.Model):
    submission_number = models.CharField(max_length=10, null=True, blank=True)
    type = models.ForeignKey(
        ServiceType,
        null = True,
        blank=True,
        on_delete = models.CASCADE,
    )
    category = models.ForeignKey(
        ServiceCategory,
        null = True,
        blank=True,
        on_delete = models.CASCADE,
    )
    is_paid = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(null=True, blank=True)

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


