ALTER TABLE checkins 
ADD CONSTRAINT fk_checkins_pois 
FOREIGN KEY (venue_id) REFERENCES pois(venue_id)