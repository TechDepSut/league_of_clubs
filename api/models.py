from django.db import models

class Club(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='clubs', blank=True, null=True)
