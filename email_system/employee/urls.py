from django.urls import path
from .views import EmployeeList, EventList, TemplateList, test

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('events/', EventList.as_view(), name='event-list'),
    path('templates/', TemplateList.as_view(), name='template-list'),
    path('test/', test, name='test'),
]