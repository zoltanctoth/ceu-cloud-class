DROP TABLE IF EXISTS {{database_name}}.bronze_edits;

CREATE EXTERNAL TABLE
{{database_name}}.bronze_edits (
    title STRING,
    edits INT,
    date DATE,
    retrieved_at TIMESTAMP) 
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://{{your bucket}}/datalake/bronze_edits/';