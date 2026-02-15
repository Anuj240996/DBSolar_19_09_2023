from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_convert_tags_to_jsonb'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='stage',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET_NULL, related_name='leads', to='leads.stage'),
        ),
        migrations.AddField(
            model_name='lead',
            name='next_follow_up',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='opportunity_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='probability',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='lead',
            name='expected_close',
            field=models.DateField(blank=True, null=True),
        ),
    ]

