from rest_framework.response import Response
from rest_framework.views import APIView

from app_goods.models import Item
from app_goods.serializers import ItemSerializer


class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
