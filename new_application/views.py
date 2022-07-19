import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def home(request):
    logger.error("Запрошена главная страница")
    return HttpResponse('Главная')

def about(request):
    logger.error("Запрошена страница 'Наш клуб'")
    return HttpResponse('Наш клуб')