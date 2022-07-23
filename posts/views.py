import logging
from django.conf import settings
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f"MY_ENV_VAR: {settings.MY_ENV_VAR}")
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    elif request.GET.get("AGE") == 18:
        logger.info(f"access:{settings.ALLOWED}")
    elif request.GET.get("AGE") < 18:
        logger.info(f"access:{settings.DENIED}")
    return HttpResponse("Posts index view")