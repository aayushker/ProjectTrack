from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('Assigned', 'Assigned'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], default='Assigned')
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Progress(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    completion_percentage = models.FloatField(default=0.0)
    score = models.IntegerField(default=0)
