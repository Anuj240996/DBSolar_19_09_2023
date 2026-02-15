from django.db import migrations


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0008_add_pipeline_fields'),
    ]

    operations = [
        # Ensure leads_opportunity table exists (in case initial migration was faked)
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS leads_opportunity (
                id bigserial PRIMARY KEY,
                lead_id bigint NOT NULL REFERENCES leads_lead(id) ON DELETE CASCADE,
                quotation_id bigint,
                total_system_cost numeric(12,2),
                subsidy numeric(12,2),
                roi numeric(6,2),
                emi numeric(12,2),
                payback_period_months integer,
                probability numeric(5,2) DEFAULT 0,
                expected_close date,
                status varchar(50) DEFAULT 'open'
            );
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        # Convert images column to jsonb if currently an array or varchar[]
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1 FROM information_schema.columns
                    WHERE table_name='leads_sitesurvey' AND column_name='images'
                ) THEN
                    -- Only run ALTER if column is not type jsonb
                    IF (SELECT pg_type.typtype FROM pg_catalog.pg_type WHERE pg_type.oid = (
                        SELECT atttypid FROM pg_catalog.pg_attribute
                        WHERE attrelid = 'leads_sitesurvey'::regclass AND attname = 'images'
                    )) IS DISTINCT FROM 'b'::char THEN
                        BEGIN
                            ALTER TABLE leads_sitesurvey ALTER COLUMN images TYPE jsonb USING to_json(images)::jsonb;
                        EXCEPTION WHEN others THEN
                            -- fallback: try casting text[] to json
                            ALTER TABLE leads_sitesurvey ALTER COLUMN images TYPE jsonb USING to_json(array_to_json(images))::jsonb;
                        END;
                    END IF;
                END IF;
            END
            $$;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunPython(noop),
    ]

