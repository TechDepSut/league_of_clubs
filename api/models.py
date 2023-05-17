from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):

    class Statuses(models.TextChoices):
        ON_ELECTION = 'on_election', 'On election'
        INACTIVE = 'inactive', 'Inactive'
        WINNER = 'winner', 'Winner'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='clubs', blank=True, null=True)
    status = models.CharField(max_length=20, choices=Statuses.choices, default=Statuses.INACTIVE)


class Winner(models.Model):
    id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    season = models.IntegerField()


class Student(models.Model):

    class TrainingForm(models.TextChoices):
        FULL_TIME = 'full_time', 'Очная'
        DISTANCE = 'distance', 'Заочная'
        FULL_TIME_AND_DISTANCE = 'full_time_and_distance', 'Очно-заочная'

    uid = models.IntegerField()
    group_number = models.CharField(max_length=10)
    faculty = models.CharField(max_length=6)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    student_credit = models.IntegerField() # номер зачетки
    course = models.IntegerField()
    training_form = models.CharField(max_length=25, choices=TrainingForm.choices, default=TrainingForm.FULL_TIME)
    age = models.IntegerField()
    email = models.EmailField()
    choise = models.BooleanField(default=False)


class Selection(models.Model):
    id = models.AutoField(primary_key=True)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    votes = models.IntegerField()
