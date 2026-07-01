from django.urls import path
from .views import yozuvlar_royxati_view, mualliflar_royxati_view

urlpatterns = [
    path('yozuvlar/', yozuvlar_royxati_view, name='yozuvlar_royxati'),
    path('mualliflar/', mualliflar_royxati_view, name='mualliflar_royxati'),
]
