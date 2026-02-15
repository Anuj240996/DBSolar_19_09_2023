from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_seed_stages'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='customer_id',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]

