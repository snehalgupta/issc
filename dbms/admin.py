from django.contrib import admin
from .models import Subtask, Projects, UserProfile

# Register your models here.

admin.site.register(Subtask)
admin.site.register(Projects)
admin.site.register(UserProfile)


