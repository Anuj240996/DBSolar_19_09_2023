# Generated by Django 3.1.4 on 2023-06-18 04:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0073_auto_20230617_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('70af39d7-9a6f-4043-93f0-9963bf2f3fb1'), primary_key=True, serialize=False),
        ),
    ]
