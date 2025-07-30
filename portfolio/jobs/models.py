from django.db import models

# Create your models here.

class Job(models.Model):
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=150)
    description=models.CharField(max_length=1000)
    year=models.CharField(max_length=10,default='2025')

    def __str__(self):
        return self.summary
