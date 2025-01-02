import pika

def get_rabbitmq_connection():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',  # Update with your RabbitMQ host
            port=5672,
            virtual_host='/',
            credentials=credentials
        )
    )
    return connection


def publish_message(queue_name, message):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Makes the message persistent
        ),
    )
    connection.close()


def consume_messages(queue_name, callback):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)

    def on_message(ch, method, properties, body):
        callback(body)  # Pass the message body to the callback
        ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge the message

    channel.basic_consume(queue=queue_name, on_message_callback=on_message)
    print(f"Waiting for messages in {queue_name}. To exit, press CTRL+C")
    channel.start_consuming()
