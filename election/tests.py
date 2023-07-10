from django.test import TestCase
from .models import Club, Student


class ClubModelTests(TestCase):
    def test_create_club(self):
        club = Club.objects.create(name='Club A', description='Club A description', votes=10)
        self.assertEqual(Club.objects.count(), 1)
        self.assertEqual(Club.objects.get().name, 'Club A')
        self.assertEqual(Club.objects.get().description, 'Club A description')
        self.assertEqual(Club.objects.get().votes, 10)

    def test_club_string_representation(self):
        club = Club.objects.create(name='Club B', description='Club B description', votes=5)
        self.assertEqual(str(club), 'Club B')

class StudentModelTests(TestCase):
    def test_create_student(self):
        club = Club.objects.create(name='Club A', description='Club A description', votes=10)
        student = Student.objects.create(uid='student1', name='John Doe', choice=club, choice2=False)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().uid, 'student1')
        self.assertEqual(Student.objects.get().name, 'John Doe')
        self.assertEqual(Student.objects.get().choice, club)
        self.assertEqual(Student.objects.get().choice2, False)

    def test_student_string_representation(self):
        club = Club.objects.create(name='Club B', description='Club B description', votes=5)
        student = Student.objects.create(uid='student2', name='Jane Smith', choice=club, choice2=True)
        self.assertEqual(str(student), 'Jane Smith')

        
