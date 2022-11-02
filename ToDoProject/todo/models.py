from django.db import models

# Create your models here.
class Task(models.Model):
    Heading = models.CharField(max_length=20)
    Details = models.CharField(max_length=20)
    Date = models.DateField()

    is_deleted =models.CharField(max_length=2,default="n")
