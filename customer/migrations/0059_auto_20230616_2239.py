# Generated by Django 3.1.4 on 2023-06-16 17:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0058_auto_20230616_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('54560395-5012-4165-886e-12a4926519b9'), primary_key=True, serialize=False),
        ),
    ]