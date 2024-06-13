INSERT INTO map_portionloire(
	nom, geometrie, arrivee_id, depart_id) VALUES ('test4',
	(WITH data AS (SELECT
		(SELECT geom::geometry FROM map_loiremodel) as line,
		ST_SetSRID(ST_MakePoint(-0.5053995, 47.4186325),4326) as point)
        SELECT ST_AsText( ST_Split( ST_Snap(line, ST_Buffer(point, 0.03), 0.03), point)) AS snapped_split
       FROM data), 20, 21)
