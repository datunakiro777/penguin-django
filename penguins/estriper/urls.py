from django.urls import path
from estriper.views import hello_estriper

urlpatterns = [
    path('estriper/', hello_estriper, name='hello')
]