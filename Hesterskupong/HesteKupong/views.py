from django.http import HttpResponse
from django.db import models
from django.views import View
from django.views import generic
from HesteKupong.models import Navnetabell
from django.shortcuts import render
# from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
import pypyodbc
from django.template import loader
from django.template.context_processors import request
# from adodbapi.test.test_adodbapi_dbapi20 import instance
def Tiden(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
#Hurra denne virker   
#     tabellnavn = Navnetabell.objects.values_list('id','first_name','last_name') 
#     testtabell = Navnetabell.objects.all()
#     tider = datetime.datetime.now()
    testtabell = Navnetabell.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(testtabell, 5) # Show 25 contacts per page
    try:
        navnetabell = paginator.page(page)
    except PageNotAnInteger:
        navnetabell = paginator.page(1)
    except EmptyPage:
        navnetabell = paginator.page(paginator.num_pages)

#     page = request.GET.get('page')
#     testtabell = paginator.get_page(page)
#     testtabell = paginator.get_page
    for i in  testtabell:
        print("%s" % i.id) 
        print("%s" % i.first_name)
        print("%s" % i.last_name)
#     tider = datetime.date 
#     now = tider
    context = {'navnetabell':  navnetabell}
# #      context = {'baneliste': baneliste}
# #      return render(request,'', context = context)
    return render(request,'index2.html', context = context)    
#     return HttpResponse(testtabell)

# #creating the values to pass
# #     now = '2040'      
#     context = {
#      'now': now,
#     }
#     return render(request,'index.html', context = context)  

# return ('index.html', {'current_date': now})
# Denne er definert VIEW for HesterTips
# def Navnetabell(request):
#     tabellnavn = Navnetabell.objects.values_list('id','first_name','last_name') 
#     for i in  tabellnavn:
# #          pass
# #          bane =(1)
#         print("%s" % i.id) 
#         print("%s" % i.first_name)
#         print("%s" % i.last_name)
#     context = {'tabellnavn':  tabellnavn}
# #      context = {'baneliste': baneliste}
# #      return render(request,'', context = context)
#     return render(request,'index.html', context = context)
#      context = {'baneliste': test6}
#      context = {'baneliste': baneliste}
#      return render(request,'banelist.html', context = context)

#     def get_queryset(self):
#         return BaneDatoOppdatert.objects.all()
#     Template_name = 'HesterTips/index.html'
#return render_to_response('index.html', {'current_date': now})