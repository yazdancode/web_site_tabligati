# admin.py
from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "fullname",
        "email",
        "phone_number",
        "subject",
        "message",
        "created_at",
    )
    search_fields = (
        "fullname",
        "email",
        "phone_number",
        "subject",
        "message",
        "created_at",
    )
