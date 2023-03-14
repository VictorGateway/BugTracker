from django.test import TestCase, SimpleTestCase
from .models import BugTracker, Developer 
from accounts.models import CustomUser
from django.urls import reverse

class BugTrackerTest(TestCase):
    'test for the bug tracker model'
    def setUp(self):
        self.bugtracker=BugTracker.objects.create( priority="low", title="This is a test title", summary="This is a test summary", status="Open", )

    def test_model_content(self):
        self.assertEqual(self.bugtracker.priority,'low')
        self.assertEqual(self.bugtracker.title, "This is a test title")
        self.assertEqual(self.bugtracker.summary, "This is a test summary")
        self.assertEqual(self.bugtracker.status, "Open")

class DeveloperTest(TestCase):
    'test for the developer model'
    def setUp(self):
        self.developer=Developer.objects.create(first_name="John", last_name="Smith", email="jsmith@exampleemail.com")

    def test_model_content(self):
        self.assertEqual(self.developer.first_name, "John")
        self.assertEqual(self.developer.last_name, "Smith")
        self.assertEqual(self.developer.email, "jsmith@exampleemail.com")

        
class CustomUserTest(TestCase):
    'test for the custom user model'
    def setUp(self):
        self.customuser=CustomUser.objects.create(email='johnsmith@gmail.com', password='samplepassword123')

    def test_model_content(self):
        self.assertEqual(self.customuser.email,'johnsmith@gmail.com')
        self.assertEqual(self.customuser.password,'samplepassword123')