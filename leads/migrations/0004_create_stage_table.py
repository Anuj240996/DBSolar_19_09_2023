from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_add_customer_id'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS leads_stage (
                id BIGSERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                "order" integer NOT NULL DEFAULT 0,
                is_won boolean NOT NULL DEFAULT false,
                is_lost boolean NOT NULL DEFAULT false
            );
            """,
            reverse_sql="""
            DROP TABLE IF EXISTS leads_stage;
            """
        )
    ]

