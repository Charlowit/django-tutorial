from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, ToDoList


def index(request, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.all()
    return HttpResponse("<h1>%s</h1></br><p>%s</br>%s</p>" %(ls.name, str(item.get(id=1)), str(item.get(id=2))))
