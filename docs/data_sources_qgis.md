## Boundries of Garching layer

Got via. Overpass API: https://overpass-turbo.eu/

```java
[out:json][timeout:25];
// Search for the administrative boundary of Garching bei München
area["name"="Garching bei München"]["admin_level"="8"]->.searchArea;
relation(area.searchArea)["boundary"="administrative"];
out body;
>;
out skel qt;
```

## Verkehrslinie layer

Got via. geopackage file () in basemap.de https://basemap.de/dienste/opendata/basisviews/basisviews_bdlm_BY_EPSG:4326_2024-11-15.gpkg

## OSM highway layer

Got via. QuickOSM Plugin in QGIS with key "highway" and filter with "Garcing, München".
