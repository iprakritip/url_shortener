from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class URL_Table(models.Model):
    original_url=models.URLField(max_length=10000)
    shortened_url=models.CharField(max_length=100)