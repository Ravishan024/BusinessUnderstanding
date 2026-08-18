import json
from shapely.geometry import shape, mapping
from shapely.ops import unary_union

SRC = "/home/claude/equity_research/india_states_gadm.geojson"
OUT = "/home/claude/equity_research/india_states_paths.json"

d = json.load(open(SRC))

# group polygons by state name, dissolve any multi-feature states (e.g. islands separate features)
by_state = {}
for f in d["features"]:
    name = f["properties"]["NAME_1"]
    geom = shape(f["geometry"])
    by_state.setdefault(name, []).append(geom)

# Drop tiny/irrelevant union territories far offshore that would blow out the bounding box unnecessarily?
# Keep all - India map should show full extent including islands is optional; drop Andaman/Lakshadweep to keep mainland focus.
DROP = {"Andaman and Nicobar", "Lakshadweep"}

simplified = {}
for name, geoms in by_state.items():
    if name in DROP:
        continue
    merged = unary_union(geoms)
    simp = merged.simplify(0.045, preserve_topology=True)
    simplified[name] = simp

# Compute overall bounds
minx = min(g.bounds[0] for g in simplified.values())
miny = min(g.bounds[1] for g in simplified.values())
maxx = max(g.bounds[2] for g in simplified.values())
maxy = max(g.bounds[3] for g in simplified.values())
print("bounds", minx, miny, maxx, maxy)

# Projection: simple equirectangular with latitude cosine correction at mean lat, then flip Y (SVG y grows downward)
import math
mean_lat = (miny + maxy) / 2
cos_lat = math.cos(math.radians(mean_lat))

SCALE = 1800.0  # px per degree roughly, will normalize after

def project(lon, lat):
    x = (lon - minx) * cos_lat
    y = (maxy - lat)  # flip
    return x, y

def poly_to_path(geom):
    parts = []
    polys = geom.geoms if geom.geom_type == "MultiPolygon" else [geom]
    for poly in polys:
        rings = [poly.exterior] + list(poly.interiors)
        for ring in rings:
            coords = list(ring.coords)
            pts = [project(lon, lat) for lon, lat in coords]
            d = "M " + " L ".join(f"{x:.2f},{y:.2f}" for x, y in pts) + " Z"
            parts.append(d)
    return " ".join(parts)

state_paths = []
for name, geom in simplified.items():
    path = poly_to_path(geom)
    state_paths.append({"name": name, "path": path})

# viewBox in projected units
proj_minx, proj_maxy = project(minx, miny)  # miny -> largest y
proj_maxx, proj_miny = project(maxx, maxy)  # maxy -> smallest y (0)
vb_x0 = 0
vb_y0 = 0
vb_w = (maxx - minx) * cos_lat
vb_h = (maxy - miny)
print("viewbox", vb_w, vb_h)

out = {
    "viewBox": f"0 0 {vb_w:.2f} {vb_h:.2f}",
    "bounds": {"minx": minx, "miny": miny, "maxx": maxx, "maxy": maxy, "cos_lat": cos_lat},
    "states": state_paths,
}
json.dump(out, open(OUT, "w"))
print("wrote", OUT, "states:", len(state_paths))
print("total path chars:", sum(len(s["path"]) for s in state_paths))
