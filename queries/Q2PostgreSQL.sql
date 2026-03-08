WITH stable_friends AS (
    SELECT user_id, friend_id FROM friendship_before
    INTERSECT
    SELECT user_id, friend_id FROM friendship_after
)
SELECT 
    sf.user_id,
    sf.friend_id,
    c.venue_id,
    c.utc_time
FROM stable_friends sf
JOIN checkins c ON sf.friend_id = c.user_id
ORDER BY c.utc_time DESC;