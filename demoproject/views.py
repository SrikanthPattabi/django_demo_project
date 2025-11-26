from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home Page")

def demo(request):
    return HttpResponse("This is demo page")