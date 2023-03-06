from django.db import models
from django.contrib.auth.models import User
import datetime

class Product(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField( default=datetime.date.today)


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True, default=1000)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    user_level = models.CharField(max_length=20, choices=[('Author', 'Author'), ('Developer', 'Developer'), ('Tester', 'Tester'), ('Admin', 'Admin')  ])



class Bugs(models.Model):
    bug_id = models.AutoField(primary_key=True, default=100)
    program = models.CharField(max_length=100)
    report_type = models.CharField(max_length=20, choices=[('Coding Error', 'Coding Error'), ('Design Issue', 'Design Issue'), ('Suggestion', 'Suggestion'), ('Documentation', 'Documentation'), ('Hardware', 'Hardware'), ('Query', 'Query')])
    problem_summary = models.TextField()
    problem = models.TextField()
    suggested_fix = models.TextField()
    reproducible = models.BooleanField(default=False)
    report_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField( default=datetime.date.today)
    functional_area = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='bugs_assigned', null=True, blank=True)
    comment = models.TextField()
    status = models.CharField(max_length=20, choices=[('Open', 'Open'), ('Closed', 'Closed')])
    priority = models.CharField(max_length=20, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    resolution = models.CharField(max_length=100)
    resolved_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tested_by = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='bugs_created')



