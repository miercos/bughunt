from django.db import models
from django.contrib.auth.models import User
import datetime

class Product(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField( default=datetime.date.today)
    version = models.CharField(max_length=100, default=0)
    release = models.CharField(max_length=100,default=0)
    

class Area(models.Model):
    area_id = models.AutoField(primary_key=True, )
    area_name = models.CharField(max_length=100, null=True)
    areas = models.CharField(max_length=300, null=True,default='')
    
    

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    emp_id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    user_level = models.CharField(max_length=20, choices=[('Author', 'Author'), ('Developer', 'Developer'), ('Tester', 'Tester'), ('Admin', 'Admin')  ])
    password = models.CharField(max_length=100,default='root')
    level = models.CharField(max_length=100,default='0',null=True)

    # def __str__(self):
    #     return self.user.username


class Bugs(models.Model):
    bug_id = models.AutoField(primary_key=True,  unique=True)
    program = models.CharField(max_length=100)
    report_type = models.CharField(max_length=20, choices=[('Coding Error', 'Coding Error'), ('Design Issue', 'Design Issue'), ('Suggestion', 'Suggestion'), ('Documentation', 'Documentation'), ('Hardware', 'Hardware'), ('Query', 'Query')],null=True)
    problem_summary = models.TextField(null=True)
    problem = models.TextField(null=True)
    suggested_fix = models.TextField(null=True)
    reproducible = models.BooleanField(default=False,null=True)
    report_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reported_bugs',null=True)
    date = models.DateField( default=datetime.date.today,null=True)
    functional_area = models.CharField(max_length=100,null=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='bugs_assigned', null=True, blank=True)
    comment = models.TextField(null=True)
    status = models.CharField(max_length=20, choices=[('Open', 'Open'), ('Closed', 'Closed')],null=True)
    priority = models.CharField(max_length=20, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')],null=True)
    resolution = models.CharField(max_length=100,null=True)
    resolved_by = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='resolved_bugs', null=True )
    area = models.ForeignKey(Area, on_delete=models.CASCADE,related_name='area', null=True )
    tested_by = models.CharField(max_length=50,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='bugs_created',null=True)



