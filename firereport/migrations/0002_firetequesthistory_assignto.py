# Generated by Django 4.1.5 on 2023-03-19 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firereport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='firetequesthistory',
            name='AssignTo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
