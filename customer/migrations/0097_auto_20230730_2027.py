# Generated by Django 3.1.4 on 2023-07-30 14:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0096_auto_20230730_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('adbe27ea-f255-41b6-9b1d-933bdc3d724a'), primary_key=True, serialize=False),
        ),
    ]