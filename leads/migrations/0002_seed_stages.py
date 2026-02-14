from django.db import migrations, connections, DEFAULT_DB_ALIAS


def create_default_stages(apps, schema_editor):
    # Ensure the leads_stage table exists before using ORM queries.
    conn = connections[DEFAULT_DB_ALIAS]
    try:
        table_names = conn.introspection.table_names()
    except Exception:
        table_names = []
    if 'leads_stage' not in table_names:
        # Table not present yet — skip seeding. It will be safe to run later.
        return

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
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_stages),
    ]

