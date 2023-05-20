from rest_framework import viewsets
from api.serializers import ClubSerializer, StudentSerializer, WinnerSerializer, SelectionSerializer
from api.models import Club, Student, Winner, Selection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


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


class VoteViewSet(viewsets.ViewSet):
    # create vote functionality, which allows you to increase the vote count of a particular club, and change the user choise value to True
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def update(self, request, pk=None):
        print(request.data)
        print(pk)
        try:
            club = Club.objects.get(pk=pk)
        except Club.DoesNotExist:
            return Response({'error': 'Club does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            selection, created = Selection.objects.get(club_id=club)
        except Selection.DoesNotExist:
            return Response({'error': 'Selection does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        selection.votes += 1
        selection.save()

        student = Student.objects.get(uid=request.data['uid'])
        student.choise = True
        student.save()

        return Response({'success': 'Vote has been created.'}, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        # print(request.data)
        queryset = Club.objects.all()
        serializer = ClubSerializer(queryset, many=True)
        return Response(serializer.data)