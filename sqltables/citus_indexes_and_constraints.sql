SET citus.multi_shard_modify_mode TO 'sequential';

ALTER TABLE checkins 
ADD CONSTRAINT fk_checkins_pois 
FOREIGN KEY (venue_id) REFERENCES pois(venue_id);

CREATE INDEX idx_checkins_user_id ON checkins (user_id);
CREATE INDEX idx_checkins_time ON checkins (utc_time);
