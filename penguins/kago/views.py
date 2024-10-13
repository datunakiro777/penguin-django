from django.shortcuts import render
from django.http import HttpResponse

def hello_kago(request):
    return HttpResponse('kago said hello')
