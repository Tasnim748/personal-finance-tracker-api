# Generated by Django 5.0.4 on 2024-04-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountManagement', '0003_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
