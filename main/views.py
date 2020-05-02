from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Desarrollado por @Charlowit!</h1>")

def v1(request):
    return HttpResponse("<h1>Segunda vista desarrollada por @Charlowit!</h1>")
