from django.shortcuts import render
from django.http import request,HttpResponse


def index(request):
    return render(request, 'index.html')
