# Generated by Django 5.0.4 on 2024-04-24 11:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_expense_person'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='paid',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expenses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expensetype',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('dueDate', models.DateField()),
                ('paid', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.CharField(max_length=50, unique=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]