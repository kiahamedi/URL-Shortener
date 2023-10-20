from django.test import TestCase, Client
from django.urls import reverse


class TestViews (TestCase):

    def setUp(self):
        self.client = Client()
        self.home_dashboard = reverse("dashboard:home")
        self.test404_dashboard = reverse("dashboard:test404")
        self.create_dashboard = reverse("dashboard:create")
        self.create_dashboard_false = reverse("dashboard:gourl", args=["test-data"])
        
    def test_home_GET(self):
        response = self.client.get(self.home_dashboard)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortner/index.html')
    
    def test_test404_GET(self):
        response = self.client.get(self.test404_dashboard)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortner/404.html')
    
    def test_create_POST(self):
        data = {
            "link": "https://127.0.0.1:8000",
            "is_expire": "true",
            "days": "1 Day",
        }
        response = self.client.post(self.create_dashboard, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content.decode("utf-8")), 5)
    
    def test_gourl_GET(self):
        # Check for True input
        data = {
            "link": "https://127.0.0.1:8000",
            "is_expire": "true",
            "days": "1 Day",
        }
        response = self.client.post(self.create_dashboard, data)
        return_data = response.content.decode("utf-8")
        self.gourl_dashboard_true = reverse("dashboard:gourl", args=[return_data])
        response = self.client.get(self.gourl_dashboard_true)
        self.assertEqual(response.status_code, 302)

        # Check for Wrong input
        response = self.client.get(self.create_dashboard_false)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'shortner/404.html')


