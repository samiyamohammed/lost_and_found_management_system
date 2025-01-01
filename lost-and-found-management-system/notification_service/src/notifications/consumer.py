import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received message: {message}")

def consume_notifications():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notifications_queue', durable=True)
    channel.basic_consume(queue='notifications_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_notifications()