cd C:\OSGeo4W64\bin

REM Intégration shapefile
ogr2ogr -f "PostgreSQL" PG:"host=localhost dbname=postgis user=postgres password=postgres port=5432" "C:\FORMATION\20210201\cadastre-etalab\parcelles.shp" -nln "formation.parcelles" -nlt MULTIPOLYGON

echo Intégration terminée avec succès
