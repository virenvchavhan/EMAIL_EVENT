from celery import shared_task
from datetime import date, time, datetime
from django.core.mail import send_mail
from .models import Employee, Event, Template, LogEntry
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


@shared_task(bind=True)
def test_func(self):
    today = date.today()
    events_today = Event.objects.filter(event_date__month=today.month, event_date__day=today.day).distinct()

    for event in events_today:
        sub = f'Congratulations for your {event.event_type}'
        from_mail = settings.EMAIL_HOST_USER
        template = Template.objects.get(event_type=event.event_type)
        msg = EmailMultiAlternatives(sub,template.content.format(name=event.employee.name, num=abs(event.event_date.year-today.year)), from_mail, [event.employee.email])
        res=msg.send()
    
@shared_task(bind=True)
def send_event_emails(*args, **kwargs):
    today = date.today()
    events_today = Event.objects.filter(event_date__month=today.month, event_date__day=today.day).distinct()

    for event in events_today:
        sub = f'Congratulations for your {event.event_type}'
        from_mail = settings.EMAIL_HOST_USER
        template = Template.objects.get(event_type=event.event_type)
        try:
            validate_email(event.employee.email)
        except ValidationError:
            LogEntry.objects.create(level="ERROR", message = f"Invalid email for the employee {event.employee.name}")
            continue


        max_retries = 5
        retries = 0

        while retries < max_retries:
            msg = EmailMultiAlternatives(sub, template.content.format(name=event.employee.name, num=abs(event.event_date.year - today.year)), from_mail, [event.employee.email])
            res = msg.send()

            if res == 1:
                LogEntry.objects.create(level="SUCCESS", message = f"Email sent successfully to {event.employee.name} for the event {event.event_type}", timestamp=datetime.now())
                print(f"Email sent successfully to {event.employee.name} for {event.event_type}")
                break  # Email sent successfully, exit the retry loop
            else:
                LogEntry.objects.create(level="WARNING", message = f"Retrying ({retries+1}) times to send email to {event.employee.name} for the event {event.event_type}", timestamp=datetime.now())
                print(f"Email sending failed for {event.employee.name} for {event.event_type}, retrying...")
                retries += 1
                time.sleep(5)  # Wait for 5 seconds before retrying

        if retries == max_retries:
            LogEntry.objects.create(level="ERROR", message = f"Email sending failed to {event.employee.name} for the event {event.event_type}", timestamp=datetime.now())
            print(f"Failed to send email to {event.employee.name} for {event.event_type} after {max_retries} retries")
