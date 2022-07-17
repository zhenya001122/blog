from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Главная')
def about(request):
    return HttpResponse('Наш клуб')