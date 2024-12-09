DROP TABLE IF EXISTS {{database_name}}.bronze_edits;

CREATE EXTERNAL TABLE
z_test.bronze_edits (
    title STRING,
    edits INT,
    date DATE,
    retrieved_at STRING) 
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://{{bucket_name}}/datalake/bronze_edits/';