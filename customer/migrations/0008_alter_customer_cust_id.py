# Generated by Django 4.1.5 on 2023-04-25 15:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_customer_cust_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('d8134435-1eb4-4ab0-a300-d4e5ded2c58b'), primary_key=True, serialize=False),
        ),
    ]
