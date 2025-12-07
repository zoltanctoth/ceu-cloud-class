DROP TABLE IF EXISTS {{database_name}}.silver_edits

CREATE TABLE {{database_name}}.silver_edits
    WITH (
          format = 'PARQUET',
          parquet_compression = 'SNAPPY',
          external_location = 's3://{{bucket-name}}/datalake/silver_edits/'
    ) AS
    SELECT 
        title,
        edits,
        date,
        cast(from_iso8601_timestamp(retrieved_at) AS TIMESTAMP) as retrieved_at
    FROM {{database_name}}.bronze_edits
