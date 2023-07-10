from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from election.models import Club, Student


class VotingSystemTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_club(self):
        response = self.client.post(
            "/api/clubs/", {"name": "Club", "description": "Test description"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Club.objects.count(), 1)
        self.assertEqual(Club.objects.get().name, "Club")
        self.assertEqual(Club.objects.get().description, "Test description")

    def test_create_student(self):
        response = self.client.post(
            "/api/students/", {"uid": "student1", "name": "Test name"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().uid, "student1")

    def test_vote(self):
        club = Club.objects.create(name="Club A", description="Test description")
        student = Student.objects.create(uid="student1", name="Test name")

        response = self.client.post(
            f"/api/students/{student.id}/vote/", {"club_id": club.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.get().choice, club)
        self.assertEqual(response.data["name"], "Club A")

        # Try voting again for the same club
        response = self.client.post(
            f"/api/students/{student.id}/vote/", {"club_id": club.id}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["info"], "You have already voted")
