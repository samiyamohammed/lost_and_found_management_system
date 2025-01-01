from celery import shared_task
from .models import LostItem, FoundItem
import pika
import json

@shared_task
def match_items():
    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()

    for lost in lost_items:
        for found in found_items:
            if lost.name.lower() in found.name.lower() and lost.location == found.location:
                message = {
                    "user_id": str(lost.user_id),  # Convert UUID to string
                    "notification": f"Your lost item '{lost.name}' has been matched with a found item!",
                }
                print(f"Debug: Message to be sent: {message}")  # Debugging statement
                publish_message('notifications_queue', message)

def publish_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    try:
        json_message = json.dumps(message)
        print(f"Debug: JSON message: {json_message}")  # Debugging statement
        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json_message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        print(f"Message sent to queue {queue_name}: {message}")
    except TypeError as e:
        print(f"Error serializing message: {e}")
    finally:
        connection.close()