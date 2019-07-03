from django.shortcuts import render
from .models import Fuck1

# Create your views here.

from django.http import HttpResponse


def hello(request):
    return HttpResponse("hello fuck")


def fuck_title(request):
    fucks = Fuck1.objects.all()
    return render(request, 'app1/titles.html', {'fucks': fucks})