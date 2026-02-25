from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending','Pending'), ('Complete','Complete'), ('In Progress','In Progress')],
        default='Pending'
    )
    priority = models.CharField(
        max_length=10,
        choices=[('Low','Low'), ('Medium','Medium'), ('High','High')],
        default='Low'
    )
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title