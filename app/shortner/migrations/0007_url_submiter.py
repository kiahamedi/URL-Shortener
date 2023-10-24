# Generated by Django 4.2.6 on 2023-10-24 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shortner", "0006_user_access_token_alter_user_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="url",
            name="submiter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shortner.user",
                verbose_name="User",
            ),
        ),
    ]
