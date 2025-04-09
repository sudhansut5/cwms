# App/admin.py
from django.contrib import admin
from .models import Process, SubProcess, CustomUser

# Register your models here.
admin.site.register(Process)
admin.site.register(SubProcess)
admin.site.register(CustomUser)
