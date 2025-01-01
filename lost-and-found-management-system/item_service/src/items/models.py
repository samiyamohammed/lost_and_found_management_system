from django.db import models
import uuid

class LostItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_lost = models.DateTimeField()
    user_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FoundItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_found = models.DateTimeField()
    user_id = models.UUIDField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
