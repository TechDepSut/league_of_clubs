from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Club, Student, Winner
from .serializers import ClubSerializer, StudentSerializer, WinnerSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=["post"])
    def vote(self, request, pk=None):
        student = self.get_object()

        if student.choice2:
            return Response(
                data={"info": "You have already voted"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        club_id = request.data.get("club_id")
        club = get_object_or_404(Club, pk=club_id)
        club.votes += 1
        club.save()
        club_serializer = ClubSerializer(club)
        student.choice = club
        student.choice2 = True
        student.save()
        return Response(club_serializer.data, status=status.HTTP_200_OK)


class WinnerViewSet(viewsets.ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer
