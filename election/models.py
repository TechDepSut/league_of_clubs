from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to="clubs/", null=True, blank=True)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Student(models.Model):
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    choice = models.ForeignKey(Club, on_delete=models.CASCADE)
    choice2 = models.BooleanField(default=False)

    def __str__(self):
        return self.name
