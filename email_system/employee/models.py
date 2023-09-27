from django.db import models

EVENT_CHOICES = [
        ('Birthday', 'Birthday'),
        ('Marriage Anniversary', 'Marriage Anniversary'),
        ('Work Anniversary', 'Work Anniversary'),
    ]

LOG_LEVEL_CHOICES = [
    ("INFO", "Info"),
    ("ERROR", "Error"), 
    ("WARNING", "Warning"),
    ("SUCCESS", "Success"),
]

class Employee(models.Model):
    emp_id = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.emp_id} - {self.name}"
        
class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    event_date = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.employee.emp_id} - {self.event_type}"
    
class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    level = models.CharField(max_length=20, choices=LOG_LEVEL_CHOICES, default="INFO")

    def __str__(self):
        return f"{self.timestamp} - {self.level}: {self.message}"
    
class Template(models.Model):
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES, unique=True)
    content = models.TextField()
    
    def __str__(self):
        return f"{self.event_type}"
    