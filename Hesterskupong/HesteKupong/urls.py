from django.shortcuts import render
from django.conf.urls import url
from HesteKupong import  views
from django.conf.urls.i18n import urlpatterns
from HesteKupong.models import Navnetabell

app_name = 'HesteKupong'
urlpatterns = [
#     url(r'',views.index, name='index'),
    url(r'',views.index, name='index'),
     ]