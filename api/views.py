from rest_framework import viewsets
from api.serializers import ClubSerializer, StudentSerializer, WinnerSerializer, SelectionSerializer
from api.models import Club, Student, Winner, Selection


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class WinnerViewSet(viewsets.ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer


class SelectionViewSet(viewsets.ModelViewSet):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer