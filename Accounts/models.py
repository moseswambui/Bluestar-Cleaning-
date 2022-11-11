from django.db import models
from django.utils.translation import gettext_lazy as _

class Accounts(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.first_name
        
    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")