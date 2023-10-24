# Generated by Django 4.2.6 on 2023-10-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortner", "0005_user_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="access_token",
            field=models.CharField(
                blank=True, max_length=200, null=True, unique=True, verbose_name="Token"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(max_length=200, unique=True, verbose_name="Phone"),
        ),
    ]
