from django.urls import path

from .views import (
    SarcheshmeView,
    AbgarmView,
    AtashkadeView,
    KaljoshView,
    EshkeneView,
    PatelepoloView,
    GolView,
    ArdeshireView,
    HalvardeView,
    NoorView,
    HotelaghsaView,
    HomeView,
    BaseBlogView,
    ContactView,
)

urlpatterns = [
    path("", BaseBlogView.as_view(), name="baseblog_view_name"),
    path("home/", HomeView.as_view(), name="home_view_name"),
    path("sarcheshme/", SarcheshmeView.as_view(), name="sarcheshme_view_name"),
    path("abgarm/", AbgarmView.as_view(), name="abgarm_view_name"),
    path("atashkade/", AtashkadeView.as_view(), name="atashkade_view_name"),
    path("kaljosh/", KaljoshView.as_view(), name="kaljosh_view_name"),
    path("eshkene/", EshkeneView.as_view(), name="eshkene_view_name"),
    path("patelepolo/", PatelepoloView.as_view(), name="patelepolo_view_name"),
    path("gol/", GolView.as_view(), name="gol_view_name"),
    path("ardeshire/", ArdeshireView.as_view(), name="ardeshire_view_name"),
    path("halvarde/", HalvardeView.as_view(), name="halvarde_view_name"),
    path("noor/", NoorView.as_view(), name="noor_view_name"),
    path("hotelaghsa/", HotelaghsaView.as_view(), name="hotelaghsa_view_name"),
    path("contact_us/", ContactView.as_view(), name="contact_us"),
]
