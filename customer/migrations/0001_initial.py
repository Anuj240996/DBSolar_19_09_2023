# Generated by Django 4.1.5 on 2023-04-23 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('salary', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('hire_date', models.DateField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.role')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Cust_id', models.IntegerField(default=uuid.UUID('56958dc8-1f7e-4ad9-b233-65cfc8cac2e3'), primary_key=True, serialize=False)),
                ('Comp_name', models.CharField(max_length=200, null=True)),
                ('Consumer', models.CharField(max_length=100, null=True)),
                ('Bill_unit', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=200, null=True)),
                ('Plant_Capacity', models.IntegerField(default=0)),
                ('Ups_Soft', models.CharField(max_length=100, null=True)),
                ('Cust_type', models.CharField(max_length=100, null=True)),
                ('City', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField(default=0)),
                ('Cus_Act_Date', models.DateField()),
                ('solar_comp', models.CharField(max_length=100, null=True)),
                ('UPSC', models.CharField(max_length=100, null=True)),
                ('Emp_id', models.IntegerField(default=0)),
                ('state', models.CharField(max_length=100, null=True)),
                ('Pincode', models.IntegerField(default=0)),
                ('phase', models.IntegerField(default=1, null=True)),
                ('loadsancution', models.IntegerField(default=0, null=True)),
                ('Gender', models.CharField(max_length=1, null=True)),
                ('new_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
