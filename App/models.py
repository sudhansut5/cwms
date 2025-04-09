from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid

class Process(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubProcess(models.Model):
    name = models.CharField(max_length=100)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PasswordResetToken(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def is_valid(self):
        # Define the validity period for the token (e.g., 24 hours)
        expiration_time = timezone.now() - timezone.timedelta(hours=24)
        return self.created_at >= expiration_time

class CustomUser(AbstractUser):
    analyst_name = models.CharField(max_length=100)
    analyst_email = models.EmailField()
    supervisor_name = models.CharField(max_length=100)
    supervisor_email = models.EmailField()
    process = models.ForeignKey(Process, on_delete=models.CASCADE,  null=True)
    sub_process = models.ForeignKey(SubProcess, on_delete=models.CASCADE, null=True)
