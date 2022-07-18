import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def home(request):
    logger.error("Test!!")
    return HttpResponse('Главная')

def about(request):
    logger.error("Test_2!!")
    return HttpResponse('Наш клуб')