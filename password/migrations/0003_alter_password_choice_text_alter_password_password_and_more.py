# Generated by Django 5.0.6 on 2024-05-30 09:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0002_password_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='choice_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='password',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to=settings.AUTH_USER_MODEL),
        ),
    ]