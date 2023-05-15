from django.contrib import admin
from .models import Club, Winner, Student

admin.site.site_header = "League of clubs"
admin.site.site_title = "League of clubs"

# Register your models here.

admin.site.register(Club)
admin.site.register(Winner)
admin.site.register(Student)
