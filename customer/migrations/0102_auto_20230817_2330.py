# Generated by Django 3.1.4 on 2023-08-17 18:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0101_auto_20230805_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('1d6c9bf1-3562-4290-a60c-c610e838efe3'), primary_key=True, serialize=False),
        ),
    ]
