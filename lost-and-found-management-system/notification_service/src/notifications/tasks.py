# from celery import shared_task
# from django.core.mail import send_mail

# @shared_task
# def send_notification(data):
#     user_email = data.get('user_email')
#     subject = data.get('subject')
#     message = data.get('message')
    
#     send_mail(
#         subject,
#         message,
#         'your-email@example.com',
#         [user_email],
#         fail_silently=False,
#     )
    
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings 


@shared_task
def send_notification(data):
    if not settings.configured:
        settings.configure()  
    print("send_notification task called with data:", data)
    
    user_email = data.get('user_email')  
    subject = data.get('subject')
    message = data.get('message')
    
    if not user_email:
        print("No email provided. Skipping notification.")
        return
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            fail_silently=False,
        )
        print("Email sent successfully to:", user_email)
    except Exception as e:
        print("Failed to send email. Error:", e)
