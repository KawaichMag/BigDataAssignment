CREATE EXTENSION IF NOT EXISTS citus;

CREATE TABLE pois (
    venue_id VARCHAR(24) PRIMARY KEY,
    latitude DOUBLE PRECISION NOT NULL,
    longitude DOUBLE PRECISION NOT NULL,
    category TEXT,
    country CHAR(2)
);

CREATE TABLE checkins (
    user_id INTEGER NOT NULL,
    venue_id VARCHAR(24),
    utc_time TIMESTAMPTZ NOT NULL,
    timezone_offset_mins INTEGER
);

CREATE TABLE friendship_before (
    user_id INTEGER,
    friend_id INTEGER,
    PRIMARY KEY (user_id, friend_id)
);

CREATE TABLE friendship_after (
    user_id INTEGER,
    friend_id INTEGER,
    PRIMARY KEY (user_id, friend_id)
);
