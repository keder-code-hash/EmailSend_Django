from unicodedata import name
from .views import *
from django.urls import path 


urlpatterns=[
    path('send_email',send_email_user,name="send_email_user"),
    path('check',check)
] 