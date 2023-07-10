from django.contrib import admin
from .models import Club, Student

admin.site.site_header = "Election Admin"
admin.site.register(Club)
admin.site.register(Student)
gg