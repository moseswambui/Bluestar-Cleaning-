from django.db import models
from django.utils.translation import gettext_lazy as _
from Services.models import Service

class Bill(models.Model):
    STATUS_PENDING, STATUS_PAID, STATUS_REVERSED = ("PENDING", "PAID", "REVERSED")
    application_submission = models.ForeignKey(
        Service,blank=True, null=True, on_delete=models.PROTECT
    )
    amount = models.CharField(max_length=50, null=True, blank=True)
    amount_paid = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(default="")
    status = models.CharField(
        max_length=10,
        choices=((STATUS_PENDING, STATUS_PENDING), (STATUS_REVERSED, STATUS_REVERSED), (STATUS_PAID, STATUS_PAID)),
        default=STATUS_PENDING,
    )
    customer_id = models.CharField(max_length=255, null=True)
    invoice_no = models.CharField(max_length=255, null=True, blank=True, unique=True)
    slug = None

    class Meta:
        verbose_name = _("Bill")
        verbose_name_plural = _("Bills")

    def __str__(self):
        return self.customer_id