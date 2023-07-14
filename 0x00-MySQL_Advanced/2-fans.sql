-- This script ranks the country origins of bands, ordered by the number of
-- (non-unique fans)
-- Requirements:
-- Import this table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans.
-- Your script can be executed on any database.


-- Selects country origins of bands ranked by countries with most fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
