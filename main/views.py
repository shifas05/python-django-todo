from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDOList, Item

# Create your views here.

def index(response): 
    return HttpResponse("<h1>tech with shif</h1>")
def v1(response): 
    return HttpResponse("<h1>view  1!</h1>")
def item(response, id): 
    ls = ToDOList.objects.get(id=id)
    item = ls.item_set.get(id=id)
    return HttpResponse("<h1>%s</h1><br><p>%s</p>" %(ls.name, item.text))   
   
