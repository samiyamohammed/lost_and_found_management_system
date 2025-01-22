import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received message: {message}")

def consume_notifications():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare exchange and bind queue
    channel.exchange_declare(exchange='lost_found_exchange', exchange_type='direct', durable=True)
    channel.queue_declare(queue='notifications_queue', durable=True)
    channel.queue_bind(exchange='lost_found_exchange', queue='notifications_queue', routing_key='notifications_queue')
    channel.basic_consume(queue='notifications_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_notifications()
