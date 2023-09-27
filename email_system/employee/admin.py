from django.contrib import admin
from .models import *

admin.site.register(Employee)
admin.site.register(Event)
admin.site.register(LogEntry)
admin.site.register(Template)

