from django.test import TestCase
from shortener.models import URL_Table
from django.contrib.auth.models import User

class URLTableTest(TestCase):
    
    def test_URL_Table(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        url = URL_Table.objects.create(original_url="www.spotify.com", user=user)
        self.assertEquals(str(url), 'www.spotify.com')
        print("IsAUrl : ",isinstance(url,URL_Table))
        self.assertTrue(isinstance(url,URL_Table))
