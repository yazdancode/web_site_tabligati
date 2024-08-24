from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm


class BaseBlogView(TemplateView):
    """
    A base view for blog templates to avoid repetitive code.
    """

    template_name = "blog/index.html"  # Define this in each subclass


class HomeView(BaseBlogView):
    template_name = "blog/index.html"


class SarcheshmeView(BaseBlogView):
    template_name = "blog/sarcheshme.html"


class AbgarmView(BaseBlogView):
    template_name = "blog/abgarm.html"


class AtashkadeView(BaseBlogView):
    template_name = "blog/atashkade.html"


class KaljoshView(BaseBlogView):
    template_name = "blog/kaljosh.html"


class EshkeneView(BaseBlogView):
    template_name = "blog/eshkene.html"


class PatelepoloView(BaseBlogView):
    template_name = "blog/patelepolo.html"


class GolView(BaseBlogView):
    template_name = "blog/gol.html"


class ArdeshireView(BaseBlogView):
    template_name = "blog/ardeshire.html"


class HalvardeView(BaseBlogView):
    template_name = "blog/halvarde.html"


class NoorView(BaseBlogView):
    template_name = "blog/noor.html"


class HotelaghsaView(BaseBlogView):
    template_name = "blog/hotelaghsa.html"


class ContactView(FormView):
    template_name = "blog/contact_us..html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_us")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "پیام شما با موفقیت ارسال شد.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "لطفاً فرم را به درستی پر کنید.")
        return super().form_invalid(form)
