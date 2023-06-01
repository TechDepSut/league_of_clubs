from rest_framework import serializers
from .models import Club, Student, Winner, Selection


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "uid",
            "group_number",
            "faculty",
            "first_name",
            "last_name",
            "patronymic",
            "student_credit",
            "course",
            "training_form",
            "age",
            "email",
        ]


class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = "__all__"


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"
