-- Replace <username> with your username (same as used in the notebook)

-- DROP VIEW IF EXISTS <username>.edits;

CREATE VIEW <username>.edits AS
    SELECT
        title,
        edits,
        date,
        cast(from_iso8601_timestamp(retrieved_at) AS TIMESTAMP) as retrieved_at
    FROM <username>.raw_edits
