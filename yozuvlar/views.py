from django.shortcuts import render
from .models import Yozuv, Muallif

def yozuvlar_royxati_view(request):
    yozuvlar = Yozuv.objects.all()
    return render(request, 'yozuvlar/yozuvlar_royxati.html', {'yozuvlar': yozuvlar})

def mualliflar_royxati_view(request):
    mualliflar = Muallif.objects.all()
    return render(request, 'yozuvlar/mualliflar_royxati.html', {'mualliflar': mualliflar})

