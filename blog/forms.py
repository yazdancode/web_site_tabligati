from django import forms
from .models import ContactMessage
from .validators import FullnameValidator, EmailValidator, Phone_Number


class ContactForm(forms.ModelForm):
    fullname_validator = FullnameValidator()
    email_validator = EmailValidator()
    phone_validator = Phone_Number()
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
        
    def clean_fullname(self):
        fullname = self.cleaned_data.get("fullname")
        return self.fullname_validator.validate(fullname)
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        return self.email_validator.validate(email)
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        return self.phone_number.validate(phone)
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    