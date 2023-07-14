-- This script lists all bands with Glam rock as their main style,
-- ranked by their longevity.
-- requirements:
-- 1) Import this table dump: metal_bands.sql.zip
-- 2) Column names must be: band_name and lifespan (in years
--    until 2022 - please use 2022 instead of YEAR(CURDATE()))
-- 3) You should use attributes formed and split for computing the lifespan
-- 4) Your script can be executed on any database


-- selects band_name and lifespan in descending order.
SELECT band_name,
CASE
    WHEN split IS NOT NULL THEN split - formed
    ELSE 2022 - formed
END AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
