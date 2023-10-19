from django.db import models

# Create your models here.
class Url(models.Model):
    ip = models.CharField(max_length=200, verbose_name="IP")
    link = models.CharField(max_length=10000, verbose_name="Link")
    uuid = models.CharField(max_length=10, verbose_name="UUID")
    is_expire = models.BooleanField(default=False, verbose_name="Is Expire")
    expire = models.DateTimeField(null=True, blank=True, verbose_name="Expire")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link