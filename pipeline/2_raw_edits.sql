-- Replace <username> with your username (same as used in the notebook and Lambda)
-- Bucket name: <username>-wikidata
-- Database name: <username>

-- DROP TABLE IF EXISTS <username>.raw_edits;

CREATE EXTERNAL TABLE
<username>.raw_edits (
    title STRING,
    edits INT,
    date DATE,
    retrieved_at STRING)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://<username>-wikidata/raw-edits/';
