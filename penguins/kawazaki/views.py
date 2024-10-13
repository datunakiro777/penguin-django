from django.shortcuts import render
from django.http import HttpResponse

def hello_kawazaki(request):
    return HttpResponse('kawazaki said hello')
