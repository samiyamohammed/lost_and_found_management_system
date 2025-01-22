# import pika
# import json

# def callback(ch, method, properties, body):
#     message = json.loads(body)
#     print(f"Received message: {message}")

# def consume_notifications():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()

#     # Declare exchange and bind queue
#     channel.exchange_declare(exchange='lost_found_exchange', exchange_type='direct', durable=True)
#     channel.queue_declare(queue='notifications_queue', durable=True)
#     channel.queue_bind(exchange='lost_found_exchange', queue='notifications_queue', routing_key='notifications_queue')
#     channel.basic_consume(queue='notifications_queue', on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()

# if __name__ == "__main__":
#     consume_notifications()
import pika
import json
import requests
from tasks import send_notification

# Configuration for the User Service
USER_SERVICE_URL = "http://user-service-url/users/{user_id}/"

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received message: {message}")
    
    user_id = message.get("user_id")
    if not user_id:
        print("No user_id in message. Skipping.")
        return

    # Fetch the user's email from User Service
    try:
        response = requests.get(USER_SERVICE_URL.format(user_id=user_id))
        response.raise_for_status()
        user_data = response.json()
        
        user_email = user_data.get("email")
        if not user_email:
            print("User email not found in User Service response. Skipping.")
            return
        
        # Prepare notification data and send it
        notification_data = {
            "user_email": user_email,
            "subject": "Lost and Found Notification",
            "message": "Your item has been matched. Please check the details!"
        }
        send_notification.delay(notification_data)
    except requests.exceptions.RequestException as e:
        print(f"Error querying User Service: {e}")

def consume_notifications():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='lost_found_exchange', exchange_type='direct', durable=True)
    channel.queue_declare(queue='notifications_queue', durable=True)
    channel.queue_bind(exchange='lost_found_exchange', queue='notifications_queue', routing_key='notifications_queue')
    channel.basic_consume(queue='notifications_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_notifications()
