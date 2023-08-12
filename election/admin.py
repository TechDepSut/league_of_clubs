from django.contrib import admin
from .models import Club, Student

admin.site.site_header = "Лига клубов админ панель"
admin.site.register(Club)
admin.site.register(Student)
