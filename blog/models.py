# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    fullname = models.CharField(max_length=100, verbose_name=_("Fullname"))
    email = models.EmailField(max_length=256, verbose_name=_("Email"))
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone number"))
    subject = models.CharField(max_length=256, verbose_name=_("Subject"))
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created_at"))

    def __str__(self):
        return f"{self.fullname} -{self.email}-{self.phone_number}-{self.subject}-{self.message} {self.created_at}"
