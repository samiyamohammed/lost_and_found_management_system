from celery import shared_task
from celery.result import AsyncResult
from .models import LostItem, FoundItem
import pika
import json
import requests

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

@shared_task
def validate_user_id(user_id):
    try:
        response = requests.get(f'http://127.0.0.1:8000/users/users/{user_id}/')
        response.raise_for_status()
        json_response = response.json()
        print(f"JSON response: {json_response}")  # Print the JSON response
        return json_response.get('is_valid', False)
    except requests.HTTPError as e:
        if e.response.status_code == 401:
            return {'error': 'Unauthorized'}
        elif e.response.status_code == 404:
            return {'error': 'User not found'}
        else:
            return {'error': 'Validation failed'}
    except requests.RequestException as e:
        print(f"Error validating user ID: {e}")
        return {'error': 'Connection error'}