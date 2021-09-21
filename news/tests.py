from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Profile

User=get_user_model()

@classmethod
class ProfileTest(TestCase):

    def setUpTestData(cls):
        User.objects.create_user("", "test", "test1234")
    
    def setUp(self):
        self.user = User.objects.get(username="test")
        
    def test_create_profile(self):
        userprofile = Profile.objects.get(user=self.user)
        self.assertTrue(isinstance(userprofile,Profile))
