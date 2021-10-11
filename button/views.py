from django.shortcuts import render
from django.http import HttpResponse

from .models import Button
# Create your views here.


def index(request):
    b = Button.objects.get(pk=1)
    return render(request, 'button/index.html', {"b": b})


def l_on_of(request):
    b = Button.objects.get(pk=1)
    if b.status == 0:
        b.status = 1
        b.save()
        stile = "background-color:#F0E68C; color:#000000"
    else:
        b.status = 0
        b.save()
        stile = "background-color:#A9A9A9; color:#ffffff"
    return render(request, 'button/on-of.html', {"b": b, 'stile': stile})


def api(request):
    b = Button.objects.get(pk=1)
    context = b.status
    return render(request, 'button/api.html', {"b": b, 'context': context})
