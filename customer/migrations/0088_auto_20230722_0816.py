# Generated by Django 3.1.4 on 2023-07-22 02:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0087_auto_20230709_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('65820bba-d535-4ca5-aec7-721071ce6314'), primary_key=True, serialize=False),
        ),
    ]
