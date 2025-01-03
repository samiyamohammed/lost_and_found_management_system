from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import LostItem, FoundItem
from .serializers import LostItemSerializer, FoundItemSerializer
from .tasks import match_items
from .tasks import validate_user_id

class LostItemViewSet(viewsets.ModelViewSet):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        validation_result = validate_user_id(user_id)
        if validation_result == True:
            serializer.save()
            match_items.delay()  # Trigger matching logic asynchronously
        else:
            return Response({'error': validation_result.get('error', 'Invalid user ID')}, status=status.HTTP_400_BAD_REQUEST)
class FoundItemViewSet(viewsets.ModelViewSet):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        validation_result = validate_user_id(user_id)
        if validation_result == True:
            serializer.save()
            match_items.delay()  # Trigger matching logic asynchronously
        else:
            return Response({'error': validation_result.get('error', 'Invalid user ID')}, status=status.HTTP_400_BAD_REQUEST)
