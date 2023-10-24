from django.db import models

# Create your models here.
class User(models.Model):
    ACCOUNT_TYPE = (
        ('n' , 'Normal'),
        ('p' , 'premium'))
    STATUS_TYPE = (
        ('a' , 'Active'),
        ('d' , 'Deactive'),
        ('b' , 'Banned'))
    phone = models.CharField(max_length=200, unique=True, verbose_name="Phone")
    otp = models.CharField(max_length=50, verbose_name="OTP")
    expire_otp = models.DateTimeField(null=True, blank=True, verbose_name="Expire OTP")
    access_token = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name="Token")
    ip = models.CharField(max_length=200, verbose_name="Last IP")
    account = models.CharField(default='n', max_length=1, choices=ACCOUNT_TYPE, verbose_name='Account Type')
    expire_premium = models.DateTimeField(null=True, blank=True, verbose_name="Expire Premium")
    status = models.CharField(default='d', max_length=1, choices=STATUS_TYPE, verbose_name='Status')

    def __str__(self):
        return self.phone



class Url(models.Model):
    submiter = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="User")
    ip = models.CharField(max_length=200, verbose_name="IP")
    link = models.CharField(max_length=10000, verbose_name="Link")
    uuid = models.CharField(max_length=10, verbose_name="UUID")
    is_expire = models.BooleanField(default=False, verbose_name="Is Expire")
    expire = models.DateTimeField(null=True, blank=True, verbose_name="Expire")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link