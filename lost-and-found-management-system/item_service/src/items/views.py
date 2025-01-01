from rest_framework import viewsets
from .models import LostItem, FoundItem
from .serializers import LostItemSerializer, FoundItemSerializer
from .tasks import match_items

class LostItemViewSet(viewsets.ModelViewSet):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    def perform_create(self, serializer):
        serializer.save()
        match_items.delay()  # Trigger matching logic asynchronously
class FoundItemViewSet(viewsets.ModelViewSet):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    def perform_create(self, serializer):
        serializer.save()
        match_items.delay()  # Trigger matching logic asynchronously
