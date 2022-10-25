-- Select your database on the UI

INSERT INTO silver_edits 
SELECT title, edits, date 
FROM bronze_edits
WHERE date IS NOT NULL
      AND date NOT IN (SELECT DISTINCT date from silver_edits)
