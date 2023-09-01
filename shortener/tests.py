import string
from django.test import TestCase
from shortener.models import URL_Table
from django.contrib.auth.models import User
from shortener.short import generate_unique_id

class URLTableTest(TestCase):
    
    def test_URL_Table(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        url = URL_Table.objects.create(original_url="www.spotify.com", user=user)
        self.assertEquals(str(url), 'www.spotify.com')
        print("IsAUrl : ",isinstance(url,URL_Table))
        self.assertTrue(isinstance(url,URL_Table))


class shorteningLogicTest(TestCase):
    
    def test_id_default_length(self):
        unique_id=generate_unique_id()
        self.assertEquals(len(unique_id),5)
        self.assertTrue(all(x in string.ascii_letters + string.digits for x in unique_id))

    def test_id_custom_length(self):
        unique_id=generate_unique_id(8)
        self.assertEquals(len(unique_id),8)
        self.assertTrue(all(x in string.ascii_letters + string.digits for x in unique_id))
