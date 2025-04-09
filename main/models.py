from django.db import models
from App.models import CustomUser  # Assuming your CustomUser model is in the App app
from django.utils import timezone
 
class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
 
class DataUtility(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
 
class Production(models.Model):
    analyst_name = models.CharField(max_length=100)
    date_received = models.DateField()
    transaction_number = models.CharField(max_length=50)
    date_reviewed = models.DateField(null=True, blank=True)
    process = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    sub_process = models.CharField(max_length=100)
    tat = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[
        ('Complete', 'Complete'),
        ('In Progress', 'In Progress'),
        ('Hold', 'Hold'),
    ])
    query = models.CharField(max_length=20, choices=[
        ('No Query', 'No Query'),
        ('Internal', 'Internal'),
        ('External', 'External'),
    ])
    notes = models.TextField()
    qc_status = models.CharField(max_length=20,choices=[
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),    
    ],blank=True,default='Pending')
    pause1 = models.DateTimeField(null=True, blank=True)
    resume1 = models.DateTimeField(null=True, blank=True)
    pause2 = models.DateTimeField(null=True, blank=True)
    resume2 = models.DateTimeField(null=True, blank=True)
    pause3 = models.DateTimeField(null=True, blank=True)
    resume3 = models.DateTimeField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    idle_time = models.DurationField(null=True, blank=True)
 
    def save(self, *args, **kwargs):
        # Calculate duration before saving
        if self.start_time and self.end_time:
            duration_obj = self.end_time - self.start_time
            self.duration = str(duration_obj).split(".")[0]  # Remove microseconds
 
        super().save(*args, **kwargs)
 
 
 
    def __str__(self):
        return f"Production - {self.transaction_number} by {self.analyst_name}"
class Quality_tracker(models.Model):
    auditor_name = models.CharField(max_length=100,null=True,blank=True)
    transaction_number = models.CharField(max_length=50,null=True,blank=True)
    Production = models.ForeignKey(Production, on_delete=models.CASCADE, related_name='Quality_tracker',null=True,blank=True)
    qdate_received = models.DateField(null=True, blank=True)
    qdate_reviewed = models.DateField(null=True, blank=True)
    qstart_time = models.DateTimeField(default=timezone.now)
    qend_time = models.DateTimeField(null=True, blank=True)
    q1_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q1_comment = models.TextField(default='',null=True, blank=True)
 
    q2_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q2_comment = models.TextField(default='',null=True, blank=True)
 
    q3_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q3_comment = models.TextField(default='',null=True, blank=True)
   
    q4_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q4_comment = models.TextField(default='',null=True, blank=True)
   
    q5_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q5_comment = models.TextField(default='',null=True, blank=True)
   
    q6_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q6_comment = models.TextField(default='',null=True, blank=True)
   
    q7_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q7_comment = models.TextField(default='',null=True, blank=True)
 
    q8_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q8_comment = models.TextField(default='',null=True, blank=True)
 
    q9_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q9_comment = models.TextField(default='',null=True, blank=True)
 
    q10_result = models.CharField(max_length=20, choices=[
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('NA', 'NA'),
    ],null=True, blank=True,default=None)
    q10_comment = models.TextField(default='',null=True, blank=True)
    final_score = models.IntegerField(null=True,blank=True)
    qnotes = models.TextField(null=True,blank=True)
    qpause1 = models.DateTimeField(null=True, blank=True)
    qresume1 = models.DateTimeField(null=True, blank=True)
    qpause2 = models.DateTimeField(null=True, blank=True)
    qresume2 = models.DateTimeField(null=True, blank=True)
    qpause3 = models.DateTimeField(null=True, blank=True)
    qresume3 = models.DateTimeField(null=True, blank=True)
    qduration = models.CharField(max_length=20, null=True, blank=True)
    qidle_time = models.DurationField(null=True, blank=True)
 
    def save(self, *args, **kwargs):
        # Calculate duration before saving
        if self.qstart_time and self.qend_time:
            qduration_obj = self.qend_time - self.qstart_time
            self.qduration = str(qduration_obj).split(".")[0]  # Remove microseconds
 
        super().save(*args, **kwargs)
 
    def save(self, *args, **kwargs):
        if not self.transaction_number and self.Production:
            self.transaction_number = self.Production.transaction_number
        super().save(*args, **kwargs)
 
    class Meta:
        ordering = ['auditor_name','transaction_number','qstart_time','qend_time','q1_result','q1_comment',
                    'q2_result','q2_comment','q3_result','q3_comment','q4_result','q4_comment','q5_result',
                    'q5_comment','q6_result','q6_comment','q7_result','q7_comment','q8_result','q8_comment',
                    'q9_result','q9_comment','q10_result','q10_comment','final_score']
 
    def __str__(self):
        return f"Quality_tracker - {self.Production.transaction_number} by {self.auditor_name}"
    

    
class DataExtraction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()