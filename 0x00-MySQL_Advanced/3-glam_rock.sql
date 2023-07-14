-- list bands with Glam rock as their main style and rank them longevity
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands WHERE style LIKE '%Glam rock%';