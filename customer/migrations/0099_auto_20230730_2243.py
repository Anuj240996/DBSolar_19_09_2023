# Generated by Django 3.1.4 on 2023-07-30 17:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0098_auto_20230730_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('674fa259-cada-4915-94ce-13d6b1e67c7a'), primary_key=True, serialize=False),
        ),
    ]
