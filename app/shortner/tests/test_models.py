from django.test import TestCase
from shortner.models import Url


class TestModels (TestCase):

    def setUp(self):
        self.link = Url.objects.create(
            ip = "127.0.0.1",
            link = "https://kiahamedi.ir",
            uuid = "8Xs21",
            is_expire = False,
        )
    
    def test_link_creation(self):
        self.assertEquals(self.link.uuid, "8Xs21")