# Generated by Django 3.1.4 on 2023-06-18 05:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0074_auto_20230618_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('50c165bc-3bca-412d-88c8-42886ae98dd4'), primary_key=True, serialize=False),
        ),
    ]
