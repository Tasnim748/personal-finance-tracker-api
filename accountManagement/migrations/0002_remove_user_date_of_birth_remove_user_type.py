# Generated by Django 5.0.4 on 2024-04-08 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
    ]
