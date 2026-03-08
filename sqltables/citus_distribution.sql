SELECT create_reference_table('pois');
SELECT create_distributed_table('checkins', 'user_id');
SELECT create_distributed_table('friendship_before', 'user_id', colocate_with => 'checkins');
SELECT create_distributed_table('friendship_after', 'user_id', colocate_with => 'checkins');
