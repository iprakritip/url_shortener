import json
import string
from django.test import TestCase, Client
from shortener.models import URL_Table
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from shortener.short import generate_unique_id
from shortener.views import shortener,redirect

class URLTableTest(TestCase):
    
    def test_URL_Table(self):
        user = User.objects.create_user(username='testuser',email='testuser@gmail.com', password='testpassword')
        url = URL_Table.objects.create(original_url="www.spotify.com", user=user)
        self.assertEqual(str(url), 'www.spotify.com')
        print("IsAUrl : ",isinstance(url,URL_Table))
        self.assertTrue(isinstance(url,URL_Table))


class shorteningLogicTest(TestCase):
    
    def test_id_default_length(self):
        unique_id=generate_unique_id()
        self.assertEqual(len(unique_id),5)
        self.assertTrue(all(x in string.ascii_letters + string.digits for x in unique_id))

    def test_id_custom_length(self):
        unique_id=generate_unique_id(8)
        self.assertEqual(len(unique_id),8)
        self.assertTrue(all(x in string.ascii_letters + string.digits for x in unique_id))


class urlPatternTest(TestCase):

    def test_shotener_url(self):
        url=reverse('shortener')
        self.assertEqual(resolve(url).func,shortener)

    def test_redirect_url(self):
        url=reverse('redirect', args=['SplYo'])
        self.assertEqual(resolve(url).func,redirect)


class shortenerViewTest(TestCase):

    def setUp(self):
        self.client=Client()
        self.user=User.objects.create_user(username='testuser',email='testuser@email.com', password='testpassword')
        self.url=""

    def test_shorterner_post_success(self):
        data = {
            "original_url": "www.facebook.com",
            "user_id": self.user.id
        }
        response=self.client.post(
            self.url,
            json.dumps(data),
            content_type='application/json',
            HTTP_ACCEPT='application/json')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),{"link-status":"received"})

    def test_page_not_found(self):
        data = {
            "original_url": "www.facebook.com",
            "user_id": 678
        }
        response=self.client.post(
            self.url,
            json.dumps(data),
            content_type='application/json',
            )

        self.assertEqual(response.status_code,404)
        self.assertEqual(response.json(),{"error": "User not found"})


class redirectViewTest(TestCase):

    def setUp(self):
        self.client=Client()
        self.url="SplYo/"

    def test_redirect_success(self):
        user = User.objects.create_user(username='testuser',email='testuser@gmail.com', password='testpassword')
        url_object=URL_Table.objects.create(original_url="www.twitter.com",user_id=user.id)
        response=self.client.post(
            self.url,
            content_type='application/json',
        )
        self.assertEqual(response.json(),{"url": url_object.original_url})