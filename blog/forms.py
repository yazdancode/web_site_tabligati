from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    fullname = forms.CharField(
        label="نام و نام خانوادگی",
        widget=forms.TextInput(attrs={"class": "contact-form"}),
    )
    email = forms.EmailField(
        label="ایمیل", widget=forms.TextInput(attrs={"class": "contact-form"})
    )
    phone_number = forms.CharField(
        label="تلفن همراه", widget=forms.TextInput(attrs={"class": "contact-form"})
    )
    subject = forms.CharField(
        label="موضوع", widget=forms.TextInput(attrs={"class": "contact-form"})
    )
    message = forms.CharField(
        label="پیام خود را برای ما بنویسید",
        widget=forms.Textarea(attrs={"class": "contact-form"}),
    )

    class Meta:
        model = ContactMessage
        fields = ["fullname", "email", "phone_number", "subject", "message"]
