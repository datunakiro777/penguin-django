from django.shortcuts import render
from django.http import HttpResponse

def hello_estriper(request):
    return HttpResponse('estriper said hello')
