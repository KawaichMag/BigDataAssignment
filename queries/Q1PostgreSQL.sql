SELECT 
    p.country, 
    COUNT(*) as total_checkins
FROM checkins c
JOIN pois p ON c.venue_id = p.venue_id
GROUP BY p.country
ORDER BY total_checkins DESC
LIMIT 10;