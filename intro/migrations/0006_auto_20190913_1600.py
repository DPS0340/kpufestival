# Generated by Django 2.2.3 on 2019-09-13 16:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0005_auto_20190913_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='intro_like_users',
            field=models.ManyToManyField(blank=True, related_name='intro_like_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
