# Generated by Django 4.1.5 on 2023-04-25 13:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_customer_cust_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('ed25185f-b97b-4960-a6e0-2ef03c48d465'), primary_key=True, serialize=False),
        ),
    ]
