# Generated by Django 3.1.4 on 2023-07-29 08:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0092_auto_20230729_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('2292c8ab-abb6-4c25-a415-673345c163a8'), primary_key=True, serialize=False),
        ),
    ]
