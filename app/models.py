from django.db import models
from more_itertools import first

# Create your models here.
class Mail_list(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
