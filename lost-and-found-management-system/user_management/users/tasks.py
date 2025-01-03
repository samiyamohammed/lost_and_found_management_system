from celery import shared_task
from .models import User

@shared_task
def validate_user_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        return True
    except User.DoesNotExist:
        return False