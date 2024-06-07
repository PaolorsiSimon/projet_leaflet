
INSERT INTO map_portionloire(
	nom, geometrie, arrivee_id, depart_id) VALUES ('test4',
												   (WITH data AS (SELECT
		(select ST_SNAP((ST_DUMP(map_loiremodel.geom,point)).geom,all_point,0.1) as the_geom 
from (select ST_Multi(ST_Union(st_expand(couche_de_point.the_geom, 0.05))) as point from couche_de_point ) as t1), 20, 21)
 