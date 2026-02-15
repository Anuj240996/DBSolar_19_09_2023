from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_seed_stages_fix'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='tags',
            field=models.JSONField(default=list, blank=True),
        ),
    ]

