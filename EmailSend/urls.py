from unicodedata import name
from .views import *
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('send_email',send_email_user,name="send_email_user"),
    path('check',check)
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)