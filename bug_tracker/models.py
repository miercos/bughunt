from django.db import models
from django.contrib.auth.models import User
import datetime

class Product(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Developer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Bugs(models.Model):
    bug_id = models.AutoField(primary_key=True, default=100)
    program = models.CharField(max_length=100)
    report_type = models.CharField(max_length=20, choices=[('Coding Error', 'Coding Error'), ('Design Issue', 'Design Issue'), ('Suggestion', 'Suggestion'), ('Documentation', 'Documentation'), ('Hardware', 'Hardware'), ('Query', 'Query')])
    problem_summary = models.TextField()
    problem = models.TextField()
    suggested_fix = models.TextField()
    reproducible = models.BooleanField(default=False)
    report_by = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField( default=datetime.date.today)
    functional_area = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='bugs_assigned', null=True, blank=True)
    comment = models.TextField()
    status = models.CharField(max_length=20, choices=[('Open', 'Open'), ('Closed', 'Closed')])
    priority = models.CharField(max_length=20, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    resolution = models.CharField(max_length=100)
    resolved_by = models.ForeignKey(Developer, on_delete=models.CASCADE)
    tested_by = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='bugs_created')



