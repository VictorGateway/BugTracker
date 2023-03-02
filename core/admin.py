from django.contrib import admin

from .models import BugTracker, Developer

admin.site.register(BugTracker)
admin.site.register(Developer)