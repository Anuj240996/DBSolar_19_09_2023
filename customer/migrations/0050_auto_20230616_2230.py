# Generated by Django 3.1.4 on 2023-06-16 17:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0049_auto_20230616_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('bfae2a2f-da61-4171-9be0-357606a73612'), primary_key=True, serialize=False),
        ),
    ]
