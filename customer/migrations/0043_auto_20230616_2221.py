# Generated by Django 3.1.4 on 2023-06-16 16:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0042_auto_20230616_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('06b3406c-5435-4eed-89c8-926632922af5'), primary_key=True, serialize=False),
        ),
    ]
