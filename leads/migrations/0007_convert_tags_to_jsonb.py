from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_add_tags_field'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            -- Convert tags column (varchar[]) to jsonb. If tags is already jsonb this will be a no-op.
            ALTER TABLE leads_lead
            ALTER COLUMN tags TYPE jsonb
            USING to_json(tags)::jsonb;
            """,
            reverse_sql="""
            -- Reverse: convert jsonb back to text[] (best-effort)
            ALTER TABLE leads_lead
            ALTER COLUMN tags TYPE text[]
            USING array(SELECT jsonb_array_elements_text(tags));
            """
        )
    ]

