from django.urls import path
from kago.views import hello_kago

urlpatterns = [
    path('kago/', hello_kago, name='hello')
]