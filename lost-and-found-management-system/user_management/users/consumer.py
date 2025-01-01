from rabbitmq_utils import consume_messages

def process_user_registration_message(body):
    print(f"Received message: {body}")
    # Process the message (e.g., log it, save to database, send email notifications, etc.)

if __name__ == '__main__':
    # Listen to the 'user_registration' queue
    consume_messages('user_registration', process_user_registration_message)
