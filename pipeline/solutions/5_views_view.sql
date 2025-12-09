-- Replace <username> with your username (same as used in the notebook and Lambda)

-- DROP VIEW IF EXISTS <username>.views;

CREATE VIEW <username>.views AS
    SELECT
        title,
        views,
        rank,
        date,
        cast(from_iso8601_timestamp(retrieved_at) AS TIMESTAMP) as retrieved_at
    FROM <username>.raw_views
