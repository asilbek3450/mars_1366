from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def teacher_page(request):
    return HttpResponse("<h1>Bu teacher sahifasi</h1>")
