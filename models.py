﻿# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    analyst_name = models.CharField(max_length=100)
    analyst_email = models.CharField(max_length=254)
    supervisor_name = models.CharField(max_length=100)
    supervisor_email = models.CharField(max_length=254)
    process = models.ForeignKey('AppProcess', models.DO_NOTHING, blank=True, null=True)
    sub_process = models.ForeignKey('AppSubprocess', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_customuser'


class AppCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AppCustomuser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_customuser_groups'
        unique_together = (('customuser', 'group'),)


class AppCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(AppCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class AppPasswordresettoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=32)
    created_at = models.DateTimeField()
    user = models.ForeignKey(AppCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_passwordresettoken'


class AppProcess(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_process'


class AppSubprocess(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    process = models.ForeignKey(AppProcess, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_subprocess'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AppCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainDatautility(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'main_datautility'


class MainProduction(models.Model):
    id = models.BigAutoField(primary_key=True)
    analyst_name = models.CharField(max_length=100)
    date_received = models.DateField()
    transaction_number = models.CharField(max_length=50)
    date_reviewed = models.DateField(blank=True, null=True)
    process = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    sub_process = models.CharField(max_length=100)
    tat = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    query = models.CharField(max_length=20)
    notes = models.TextField()
    pause1 = models.DateTimeField(blank=True, null=True)
    resume1 = models.DateTimeField(blank=True, null=True)
    pause2 = models.DateTimeField(blank=True, null=True)
    resume2 = models.DateTimeField(blank=True, null=True)
    pause3 = models.DateTimeField(blank=True, null=True)
    resume3 = models.DateTimeField(blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    idle_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_production'


class MainQualityData(models.Model):
    id = models.BigAutoField(primary_key=True)
    analyst_name = models.CharField(max_length=100)
    date_received = models.DateField()
    transaction_number = models.CharField(max_length=50)
    date_reviewed = models.DateField(blank=True, null=True)
    process = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    sub_process = models.CharField(max_length=100)
    tat = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    query = models.CharField(max_length=20)
    notes = models.TextField()
    pause1 = models.DateTimeField(blank=True, null=True)
    resume1 = models.DateTimeField(blank=True, null=True)
    pause2 = models.DateTimeField(blank=True, null=True)
    resume2 = models.DateTimeField(blank=True, null=True)
    pause3 = models.DateTimeField(blank=True, null=True)
    resume3 = models.DateTimeField(blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    idle_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_quality_data'


class MainReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'main_report'
