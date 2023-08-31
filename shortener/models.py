from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class URL_Table(models.Model):
    original_url=models.URLField(max_length=10000)
    shortened_url=models.CharField(max_length=100)
    count=models.IntegerField (default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self) :
        return self.original_url