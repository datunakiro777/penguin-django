from django.shortcuts import render
from django.http import HttpResponse

def hello_krico(request):
    return HttpResponse('krico said hello')
