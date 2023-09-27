from rest_framework import generics
from .models import Employee, Event, Template
from .serializers import EmployeeSerializer, EventSerializer, TemplateSerializer
from .tasks import send_event_emails, test_func
from django.http import HttpResponse


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TemplateList(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer



def send_event_mail(request):
    send_event_emails.delay()
    return HttpResponse("Sent!")

def test(request):
    test_func.delay()
    return HttpResponse("Done!")




