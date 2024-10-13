from django.urls import path
from kawazaki.views import hello_kawazaki

urlpatterns = [
    path('kawazaki/', hello_kawazaki, name='hello')
]