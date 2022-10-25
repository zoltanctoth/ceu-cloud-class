-- ADD THE ATHENA SQL SCRIPT HERE WHICH CREATES THE `bronze_edits` TABLE
CREATE EXTERNAL TABLE
{{fill in your database's name}}.bronze_edits (
    title STRING,
    edits INT,
    date DATE,
    retrieved_at TIMESTAMP) 
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://{{fill in your bucket''s name}}/datalake/edits/';


-- Check your results in a new query:
-- 1) Select your database in the UI
-- 2) SELECT date, count(*) FROM bronze_edits GROUP BY date ORDER BY date;
