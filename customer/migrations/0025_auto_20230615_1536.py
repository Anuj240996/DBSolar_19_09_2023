# Generated by Django 3.1.4 on 2023-06-15 10:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0024_auto_20230612_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('6b3c11e0-c2ef-45cb-99e9-770fe3fda151'), primary_key=True, serialize=False),
        ),
    ]