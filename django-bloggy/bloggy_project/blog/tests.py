from django.test import TestCase

# Create your tests here.
from models import Post

class PostTests(TestCase):
    """docstring for PostTsets"""
    def rest_str(self):
        my_title=Post(title='This is a basic title for a basic test case')
        self.assertEquals(
        str(my_title),'This is a basic title for a basic test case',
        )
