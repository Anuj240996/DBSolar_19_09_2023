# Generated by Django 3.1.4 on 2023-06-10 13:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_alter_customer_cust_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('3674580e-35a2-4fa3-b67d-29d8a94e11d3'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='emp_id',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]