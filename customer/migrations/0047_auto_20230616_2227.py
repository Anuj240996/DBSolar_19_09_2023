# Generated by Django 3.1.4 on 2023-06-16 16:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0046_auto_20230616_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('eefbe5b9-729e-45fb-8e4a-0ccc4dcba15e'), primary_key=True, serialize=False),
        ),
    ]