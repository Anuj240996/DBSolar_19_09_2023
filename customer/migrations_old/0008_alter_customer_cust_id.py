# Generated by Django 4.1.5 on 2023-04-23 05:23

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
            field=models.IntegerField(default=uuid.UUID('58b3535c-d4f9-4b72-a18f-55abc3415b6b'), primary_key=True, serialize=False),
        ),
    ]