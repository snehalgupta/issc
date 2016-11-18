from django.contrib import admin
from .models import Subtask, Project, UserProfile

# Register your models here.

admin.site.register(Subtask)
admin.site.register(Project)
admin.site.register(UserProfile)


