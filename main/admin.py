# App/admin.py
from django.contrib import admin
from .models import Production,Quality_tracker

# Register your models here.
admin.site.register([Production,Quality_tracker])

