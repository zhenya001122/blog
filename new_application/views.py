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

def users(request):
    logger.error("Запрошена страница 'Пользователи'")
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "User id: {0}  name: {1}".format(id, name)
    return HttpResponse(output)