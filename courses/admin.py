import secrets
from django.contrib import admin
from .models import Course,Sector,Comment,Course_section,Episode
# Register your models here.

admin.site.register(Course)
admin.site.register(Sector)
admin.site.register(Comment)
admin.site.register(Course_section)
admin.site.register(Episode)
