# Generated by Django 4.1.10 on 2023-09-02 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0009_memberingroups_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberingroups',
            name='email',
        ),
        migrations.AddField(
            model_name='memberingroups',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]