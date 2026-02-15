from django.db import migrations


def seed_default_stages(apps, schema_editor):
    Stage = apps.get_model('leads', 'Stage')
    default = [
        ('New Leads', 0, False, False),
        ('Qualified', 1, False, False),
        ('Survey', 2, False, False),
        ('Quote', 3, False, False),
        ('Negotiation', 4, False, False),
        ('Won', 5, True, False),
        ('Lost', 6, False, True),
    ]
    for name, order, is_won, is_lost in default:
        Stage.objects.update_or_create(name=name, defaults={'order': order, 'is_won': is_won, 'is_lost': is_lost})


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_create_stage_table'),
    ]

    operations = [
        migrations.RunPython(seed_default_stages, migrations.RunPython.noop),
    ]

