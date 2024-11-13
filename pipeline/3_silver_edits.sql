 CREATE TABLE {{database_name}}.silver_edits
    WITH (
          format = 'PARQUET',
          parquet_compression = 'SNAPPY',
          external_location = 's3://{{your bucket}}/datalake/silver_edits/'
    ) AS SELECT * FROM {{database_name}}.bronze_edits