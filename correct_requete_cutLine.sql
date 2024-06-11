INSERT INTO map_portionloire (nom, arrivee_id, depart_id, geometrie)
SELECT
  'Nouvelle portion',
  21,
  20,
    ST_LineSubstring(line.geom, ST_LineLocatePoint(line.geom, point_depart), ST_LineLocatePoint(line.geom, point_arrivee))
FROM
  (SELECT ST_LineMerge(map_loiremodel.geom) AS geom FROM map_loiremodel) AS line,
  (SELECT ST_GeomFromText('POINT(3.078115944662238 47.024171356379767)', 4326) AS point_depart) AS pd,
  (SELECT ST_GeomFromText('POINT(3.066907648714422 47.046509257487159)', 4326) AS point_arrivee) AS pa;