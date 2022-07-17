from django.http import HttpResponse


def index(request):
   return HttpResponse("Posts index view")
