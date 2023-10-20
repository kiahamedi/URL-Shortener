from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from shortner.views import (
    home,
    create,
    gourl,
    test404,
)
import json


client = Client()

class TestUrls (SimpleTestCase):
    databases = {"default"}
    allow_database_queries = True

    def test_home_url_is_resolved(self):
        url = reverse("dashboard:home")
        self.assertEquals(resolve(url).func, home)
    
    def test_create_url_is_resolved(self):
        data = {
        "link": "https://127.0.0.1:8000",
        "is_expire": "true",
        "days": "1 Day",
        }
        response = self.client.post(reverse("dashboard:create"),data)
        self.assertEqual(response.status_code, 200)
    
    def test_gourl_url_is_resolved(self):
        url = reverse("dashboard:gourl", args=['some-slug'])
        self.assertEquals(resolve(url).func, gourl)
    
    def test_test404_url_is_resolved(self):
        url = reverse("dashboard:test404")
        self.assertEquals(resolve(url).func, test404)