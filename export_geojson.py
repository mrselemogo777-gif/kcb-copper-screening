from pathlib import Path
import geopandas as gpd

OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

COPPER_GDB = Path.home() / "Downloads/mining_data/global_copper/USGS_global_copper.gdb"

tracts = gpd.read_file(COPPER_GDB, layer="sedCu_tracts").cx[20:30, -27:-17].to_crs(32734)
tracts.to_crs(4326).to_file(OUT / "kcb_tract.geojson", driver="GeoJSON")
print(f"kcb_tract.geojson  — {len(tracts)} feature(s)")

anchors = gpd.GeoDataFrame(
    {"name": ["Khoemacau", "Motheo"]},
    geometry=gpd.points_from_xy([22.6431, 26.9718], [-21.0944, -22.5179]),
    crs=4326,
)
anchors.to_file(OUT / "anchors.geojson", driver="GeoJSON")
print(f"anchors.geojson   — {len(anchors)} feature(s)")
