import osmnx as ox
from osmnx import projection, _overpass

if __name__ == "__main__":

    geodata_frame = ox.geocode_to_gdf("Garching, Bavaria, Germany", which_result=None)["geometry"].unary_union
    
    poly_proj, crs_utm = projection.project_geometry(geodata_frame)
    poly_proj_buff = poly_proj.buffer(500)
    poly_buff, _ = projection.project_geometry(poly_proj_buff, crs=crs_utm, to_latlong=True)

    response_jsons = _overpass._download_overpass_network(poly_buff, "all", None)
    i = 0
    for response_json in response_jsons:
        print(response_json)
        break
