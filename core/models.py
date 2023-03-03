from django.db import models
# from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


priority_choices=(('low', 'low'), ('medium', 'medium'), ('high', 'high'))
progress=(("Open", "Open"),("Closed", "Closed"),("In Progress", "In Progress"))

#try using to_field here for setting default user
class Developer(models.Model):
    first_name = models.CharField(max_length=30,)
    last_name = models.CharField(max_length=30,)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("developer_list")
  

class BugTracker(models.Model):
    project_number= models.AutoField(primary_key=True)
    assignee=  models.ForeignKey(Developer, on_delete=models.CASCADE, null=True)
    priority = models.CharField(max_length=10, choices=priority_choices)
    title = models.CharField(max_length=70)
    summary=models.TextField()
    status= models.CharField(max_length=20, choices=progress, default="Open")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.summary

    def get_absolute_url(self): 
        return reverse("bug_list")


