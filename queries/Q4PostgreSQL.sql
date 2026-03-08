SELECT 
    custom_category,
    COUNT(*) as venue_count
FROM (
    SELECT 
        CASE 
            WHEN category ILIKE '%restaurant%' THEN 'Restaurant'
            WHEN category ILIKE '%club%' THEN 'Club'
            WHEN category ILIKE '%museum%' THEN 'Museum'
            WHEN category ILIKE '%shop%' OR category ILIKE '%store%' THEN 'Shop'
            ELSE 'Others'
        END as custom_category
    FROM pois
) sub
GROUP BY custom_category;