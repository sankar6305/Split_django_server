# Generated by Django 4.1.10 on 2023-08-31 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_groupmember_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='emails',
            field=models.CharField(max_length=400),
        ),
    ]
