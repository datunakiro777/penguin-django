from django.urls import path
from krico.views import hello_krico

urlpatterns = [
    path('krico/', hello_krico, name='hello')
]