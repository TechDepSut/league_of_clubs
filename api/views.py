from rest_framework import viewsets, status
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from api.serializers import (
    ClubSerializer,
    StudentSerializer,
    WinnerSerializer,
    SelectionSerializer,
)
from api.models import Club, Student, Winner, Selection
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import (
    HttpResponseNotFound,
    HttpResponse,
    HttpResponseNotAllowed,
    HttpRequest,
)
from django.views.decorators.csrf import csrf_exempt


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class WinnerViewSet(viewsets.ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer


class VoteViewSet(viewsets.ViewSet):
    # create vote functionality, which allows you to increase the vote count of a particular club, and change the user choise value to True
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def __init__(self, uid=None, club_id=None, request=None, **kwargs):
        super().__init__(**kwargs)
        self.uid = uid
        self.club_id = club_id
        self.request = request

    @renderer_classes(JSONRenderer)
    @csrf_exempt
    def post(self, request):
        uid = self.request.POST.get("uid")
        club_id = self.request.POST.get("club_id")

        # Получение объекта модели "Club" с помощью значения переменной "club_id".
        club = get_object_or_404(Club, id=club_id, status="on_election")

        # Получение объекта модели "Selection" с помощью значения переменной "club_id".
        selection = get_object_or_404(Selection, club=club)

        # Увеличение значения поля "votes" объекта "selection" на 1 и сохранение изменений.
        selection.votes += 1
        selection.save()

        # Получение объекта модели "Student" с помощью значения поля "uid" из запроса пользователя.
        student = get_object_or_404(Student, uid=uid)

        # Установка значения поля "choice" объекта "student" на True и сохранение изменений.
        student.choice = True
        student.save()

        # Возвращает сообщение об успешном учёте голоса со статусом 201.
        return Response("Vote counted", status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = Club.objects.all()
        serializer = ClubSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            return self.post(request, *args, **kwargs)
        elif request.method == "GET":
            return self.get(request)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def update(self, request, pk=None):
    #     print(request.data)
    #     print(pk)
    #     try:
    #         club = Club.objects.get(pk=pk)
    #     except Club.DoesNotExist:
    #         return Response({'error': 'Club does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     try:
    #         selection, created = Selection.objects.get(club_id=club)
    #     except Selection.DoesNotExist:
    #         return Response({'error': 'Selection does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    #     selection.votes += 1
    #     selection.save()
    #
    #     student = Student.objects.get(uid=request.data['uid'])
    #     student.choise = True
    #     student.save()
    #
    #     return Response({'success': 'Vote has been created.'}, status=status.HTTP_201_CREATED)

    # def list(self, request):
    #     # print(request.data)
    #     queryset = Club.objects.all()
    #     serializer = ClubSerializer(queryset, many=True)
    #     return Response(serializer.data)
