import logging
from django.conf import settings
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    # if logger.info({settings.BBBB}):
    logger.info(f"MY_ENV_VAR: {settings.MY_ENV_VAR}")
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    return HttpResponse("Posts index view")