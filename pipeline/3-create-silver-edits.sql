CREATE TABLE {{fill in your database's name}}.silver_edits
    WITH (
          format = 'PARQUET',
          parquet_compression = 'SNAPPY',
          external_location = 's3://{{fill in your bucket''s name}}/datalake/silver_edits'
    ) AS SELECT title, edits, date
         FROM {{fill in your database's name}}.bronze_edits 
         WHERE date IS NOT NULL;

SELECT date, count(*) FROM silver_edits GROUP BY date ORDER BY date;