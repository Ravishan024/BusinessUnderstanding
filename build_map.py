import json

states_data = json.load(open("/home/claude/equity_research/india_states_paths.json"))

LOCATIONS = [
    # Integrated plants (captive limestone + kiln)
    {"name": "Aditya Cement Works", "city": "Shambhupura, Chittorgarh", "state": "Rajasthan", "type": "integrated", "lat": 24.88, "lon": 74.62,
     "note": "Integrated plant with captive limestone mines.", "risk": "water"},
    {"name": "Vikram Cement Works", "city": "Khor, Neemuch", "state": "Madhya Pradesh", "type": "integrated", "lat": 24.47, "lon": 74.87,
     "note": "One of UltraTech's original large integrated plants (formerly Grasim).", "risk": None},
    {"name": "Hirmi Cement Works", "city": "Hirmi, near Bilaspur", "state": "Chhattisgarh", "type": "integrated", "lat": 21.93, "lon": 81.85,
     "note": "Integrated plant with captive limestone mining nearby.", "risk": "mining"},
    {"name": "Rawan Cement Works", "city": "Rawan, Baloda Bazar", "state": "Chhattisgarh", "type": "integrated", "lat": 21.65, "lon": 82.15,
     "note": "Integrated plant; local mining operations have drawn community concerns (reported land/water disputes).", "risk": "mining"},
    {"name": "Awarpur Cement Works", "city": "Awarpur, Chandrapur", "state": "Maharashtra", "type": "integrated", "lat": 19.90, "lon": 79.40,
     "note": "Integrated plant in Vidarbha region.", "risk": None},
    {"name": "Gujarat Cement Works", "city": "Jafrabad, Amreli", "state": "Gujarat", "type": "integrated", "lat": 20.87, "lon": 71.37,
     "note": "Coastal integrated plant — enables clinker/cement shipment by sea as well as road/rail.", "risk": "cyclone"},
    {"name": "Andhra Pradesh Cement Works", "city": "Tadipatri, Anantapur", "state": "Andhra Pradesh", "type": "integrated", "lat": 14.91, "lon": 78.01,
     "note": "Integrated plant serving the South-East region.", "risk": "water"},
    {"name": "Jaggayyapeta Plant", "city": "Jaggayyapeta, Krishna", "state": "Andhra Pradesh", "type": "integrated", "lat": 16.89, "lon": 80.10,
     "note": "Integrated plant (Balaji Cement Works area).", "risk": None},
    {"name": "Dalla Cement Works", "city": "Dalla, Sonbhadra", "state": "Uttar Pradesh", "type": "integrated", "lat": 24.19, "lon": 83.06,
     "note": "Integrated plant in UP's mineral-rich Sonbhadra belt.", "risk": "mining"},
    {"name": "Manawar Plant", "city": "Manawar, Dhar", "state": "Madhya Pradesh", "type": "integrated", "lat": 22.22, "lon": 74.98,
     "note": "Integrated plant in western MP.", "risk": None},

    # Grinding units (finish clinker into cement, closer to demand — no captive mine needed on-site)
    {"name": "Arakkonam Grinding Unit", "city": "Arakkonam", "state": "Tamil Nadu", "type": "grinding", "lat": 13.08, "lon": 79.67,
     "note": "Grinding unit running on 100% renewable energy.", "risk": None},
    {"name": "Ginigera Grinding Unit", "city": "Ginigera, Koppal", "state": "Karnataka", "type": "grinding", "lat": 15.40, "lon": 76.20,
     "note": "Grinding unit running on 100% renewable energy.", "risk": None},
    {"name": "Karur Grinding Unit", "city": "Karur", "state": "Tamil Nadu", "type": "grinding", "lat": 10.95, "lon": 78.08,
     "note": "Slag-based grinding capacity, commissioned Feb 2025.", "risk": None},
    {"name": "Visakhapatnam Grinding Unit", "city": "Visakhapatnam", "state": "Andhra Pradesh", "type": "grinding", "lat": 17.70, "lon": 83.30,
     "note": "Coastal grinding unit; expansion planned. Coastal location = cyclone exposure.", "risk": "cyclone"},
    {"name": "Dhule Grinding Unit", "city": "Dhule", "state": "Maharashtra", "type": "grinding", "lat": 20.90, "lon": 74.80,
     "note": "Greenfield grinding unit, commissioned Dec 2022.", "risk": None},
    {"name": "Nagpur Grinding Unit", "city": "Nagpur", "state": "Maharashtra", "type": "grinding", "lat": 21.15, "lon": 79.09,
     "note": "Grinding unit serving Vidarbha/central India demand.", "risk": None},
    {"name": "Jhajjar Grinding Unit", "city": "Jhajjar", "state": "Haryana", "type": "grinding", "lat": 28.61, "lon": 76.65,
     "note": "Serves Delhi-NCR demand; NCR is subject to GRAP pollution-control curbs that can restrict industrial/construction activity in winter.", "risk": "pollution"},
    {"name": "Panipat Grinding Unit", "city": "Panipat", "state": "Haryana", "type": "grinding", "lat": 29.39, "lon": 76.97,
     "note": "Serves north Delhi-NCR demand; same GRAP exposure as Jhajjar.", "risk": "pollution"},
    {"name": "Bihar Grinding Unit (approx.)", "city": "Bihar", "state": "Bihar", "type": "grinding", "lat": 25.60, "lon": 85.10,
     "note": "Approximate location — exact site not yet confirmed; flagged for follow-up research.", "risk": None},
    {"name": "West Bengal Grinding Unit (approx.)", "city": "West Bengal", "state": "West Bengal", "type": "grinding", "lat": 22.60, "lon": 88.40,
     "note": "Approximate location — exact site not yet confirmed; flagged for follow-up research.", "risk": None},

    # Bulk terminals / RMC & distribution hubs (representative — company operates 10 bulk terminals & 400+ RMC plants nationally)
    {"name": "Mumbai Bulk Terminal (representative)", "city": "Mumbai", "state": "Maharashtra", "type": "hub", "lat": 19.05, "lon": 72.88,
     "note": "Representative coastal bulk terminal / major RMC demand hub — one of ~10 bulk terminals nationally.", "risk": "cyclone"},
    {"name": "Chennai Bulk Terminal (representative)", "city": "Chennai", "state": "Tamil Nadu", "type": "hub", "lat": 13.08, "lon": 80.27,
     "note": "Representative coastal bulk terminal / major RMC demand hub.", "risk": "cyclone"},
    {"name": "Kolkata Bulk Terminal (representative)", "city": "Kolkata", "state": "West Bengal", "type": "hub", "lat": 22.57, "lon": 88.36,
     "note": "Representative coastal bulk terminal / major RMC demand hub — East coast is cyclone-exposed (Bay of Bengal).", "risk": "cyclone"},
    {"name": "Delhi NCR RMC Hub (representative)", "city": "Delhi NCR", "state": "Delhi", "type": "hub", "lat": 28.61, "lon": 77.21,
     "note": "Largest urban RMC demand cluster; subject to GRAP construction curbs in winter.", "risk": "pollution"},
]

RISK_NOTES = {
    "mining": {"label": "Mining / land & community risk", "detail": "Limestone mining leases and land acquisition near these sites have drawn reported community and environmental disputes."},
    "cyclone": {"label": "Cyclone / coastal weather risk", "detail": "Coastal facilities on the Arabian Sea or Bay of Bengal are exposed to cyclone season disruption (typically Apr-Jun and Oct-Dec)."},
    "water": {"label": "Water stress risk", "detail": "Located in relatively water-stressed regions; cement grinding, captive power and RMC operations all need a reliable water supply."},
    "pollution": {"label": "Pollution-curb / GRAP risk", "detail": "Delhi-NCR's Graded Response Action Plan (GRAP) can restrict construction and industrial activity during high-pollution winter periods, hitting demand and dispatch."},
}

TYPE_META = {
    "integrated": {"label": "Integrated plant (captive limestone + kiln)", "color": "#2a78d6"},
    "grinding": {"label": "Grinding unit", "color": "#eb6834"},
    "hub": {"label": "Bulk terminal / RMC & distribution hub", "color": "#1baf7a"},
}

INTL = [
    {"country": "UAE", "city": "Ras Al Khaimah", "flag": "🇦🇪", "type": "Equity stake (31.6%) — RAK Cement Co. for White Cement & Construction Materials (RAKWCT)",
     "note": "UltraTech, via its wholly-owned UAE subsidiary UltraTech Cement Middle East Investments Ltd (UCMEIL), offered to acquire a 31.6% stake in Abu Dhabi-listed RAKWCT for roughly ₹840 crore ($101m) — a minority stake, not a fully-owned plant.",
     "risk": "Gulf-region geopolitical and currency (AED) exposure; minority stake means less operating control than a wholly-owned plant.",
     "source": "Business Standard, 2024"},
    {"country": "Bahrain", "city": "Al Hidd", "flag": "🇧🇭", "type": "Wholly-owned grinding plant — UltraTech Cement Bahrain Co. WLL",
     "note": "A grinding/terminal operation on Bahrain's Al Hidd industrial peninsula, serving Gulf demand.",
     "risk": "Small single-site exposure to Gulf demand and shipping routes through the Strait of Hormuz.",
     "source": "Global Energy Monitor / Cemnet"},
    {"country": "Sri Lanka", "city": "Peliyagoda / Kelaniya (near Colombo)", "flag": "🇱🇰", "type": "Wholly-owned grinding/packing plant — UltraTech Cement Lanka (Pvt) Ltd",
     "note": "Grinding and packing unit near Colombo port, serving the Sri Lankan domestic market.",
     "risk": "Exposure to Sri Lanka's currency and economic volatility (the country went through a severe economic/forex crisis in 2022).",
     "source": "Company directory listings"},
]
INTL_NOTE = "UltraTech also previously held cement assets in Bangladesh, which were divested (stake sold to HeidelbergCement) around 2015-16 — no longer part of current international operations."
INTL_SCALE_NOTE = "Scale check: India domestic grey cement capacity alone crossed 200 MTPA in FY2025-26, while total consolidated (India + international) capacity has been reported around 205 MTPA in recent years — implying international operations are a small single-digit percentage of total capacity. The core investment case is still almost entirely about the Indian business; the international units are a minority diversification, not a second engine of growth. (Exact current revenue/capacity split not yet researched — flagged for follow-up.)"

bounds = states_data["bounds"]

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UltraTech Cement — India Footprint & Regional Risk Map</title>
<style>
  .viz-root {
    color-scheme: light;
    --surface-1:      #fcfcfb;
    --surface-2:      #f4f3f0;
    --surface-3:      #eceae5;
    --border:         #ddd9d2;
    --text-primary:   #0b0b0b;
    --text-secondary: #52514e;
    --text-muted:     #83817a;
    --accent:         #2a78d6;
    --accent-soft:    #e7f0fb;
    --map-fill:       #eeece7;
    --map-stroke:     #cfccc3;
    --good:           #0ca30c;
    --warning:        #fab219;
    --critical:       #d03b3b;
    --warning-bg:     #fff4dd;
  }
  @media (prefers-color-scheme: dark) {
    :root:where(:not([data-theme="light"])) .viz-root {
      color-scheme: dark;
      --surface-1: #1a1a19; --surface-2: #232322; --surface-3: #2c2c2a; --border: #3a3a37;
      --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #8f8d84;
      --accent: #3987e5; --accent-soft: #17263a; --map-fill: #2a2a27; --map-stroke: #45443f;
      --good: #0ca30c; --warning: #fab219; --critical: #e66767; --warning-bg: #3a2c0e;
    }
  }
  :root[data-theme="dark"] .viz-root {
    color-scheme: dark;
    --surface-1: #1a1a19; --surface-2: #232322; --surface-3: #2c2c2a; --border: #3a3a37;
    --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #8f8d84;
    --accent: #3987e5; --accent-soft: #17263a; --map-fill: #2a2a27; --map-stroke: #45443f;
    --good: #0ca30c; --warning: #fab219; --critical: #e66767; --warning-bg: #3a2c0e;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif; background: var(--surface-1); color: var(--text-primary); }
  .viz-root { background: var(--surface-1); min-height: 100vh; padding: 26px 24px 50px; }
  .wrap { max-width: 1200px; margin: 0 auto; }
  .top-bar { display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; }
  h1 { font-size: 21px; margin: 0 0 4px; }
  .subtitle { color: var(--text-secondary); font-size: 13.5px; margin: 0 0 18px; max-width: 760px; line-height: 1.5; }
  .theme-toggle { background: var(--surface-2); border: 1px solid var(--border); color: var(--text-secondary); border-radius: 8px; padding: 6px 12px; font-size: 12px; cursor: pointer; white-space: nowrap; }
  .theme-toggle:hover { background: var(--surface-3); }

  .controls { display: flex; flex-wrap: wrap; gap: 18px; align-items: center; margin-bottom: 16px; padding: 12px 14px; background: var(--surface-2); border: 1px solid var(--border); border-radius: 10px; }
  .control-group { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
  .control-label { font-size: 11px; text-transform: uppercase; letter-spacing: .03em; color: var(--text-muted); font-weight: 700; margin-right: 2px; }
  .chip-toggle { display: flex; align-items: center; gap: 6px; font-size: 12.5px; color: var(--text-secondary); cursor: pointer; user-select: none; background: var(--surface-1); border: 1px solid var(--border); border-radius: 999px; padding: 5px 11px 5px 8px; }
  .chip-toggle input { accent-color: var(--accent); }
  .chip-dot { width: 9px; height: 9px; border-radius: 50%; flex: none; }
  .risk-toggle-btn { font-size: 12.5px; color: var(--text-primary); background: var(--surface-1); border: 1px solid var(--border); border-radius: 999px; padding: 6px 13px; cursor: pointer; font-weight: 600; }
  .risk-toggle-btn.on { background: var(--warning-bg); border-color: var(--warning); color: #a8720c; }
  :root[data-theme="dark"] .risk-toggle-btn.on { color: var(--warning); }

  .content { display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(280px, 1fr); gap: 18px; align-items: start; }
  .map-panel { background: var(--surface-2); border: 1px solid var(--border); border-radius: 12px; padding: 14px; }
  svg.mapsvg { width: 100%; height: auto; display: block; }
  .state-path { fill: var(--map-fill); stroke: var(--map-stroke); stroke-width: 0.06; transition: fill .15s ease; }
  .state-path.risk-mining { fill: #f3d9d0; }
  .state-path.risk-cyclone { fill: #d8e6f7; }
  .state-path.risk-water { fill: #f6e6c8; }
  .state-path.risk-pollution { fill: #e6ded0; }
  :root[data-theme="dark"] .state-path.risk-mining { fill: #4a3128; }
  :root[data-theme="dark"] .state-path.risk-cyclone { fill: #1f3350; }
  :root[data-theme="dark"] .state-path.risk-water { fill: #4a3a17; }
  :root[data-theme="dark"] .state-path.risk-pollution { fill: #3a352a; }

  .marker { cursor: pointer; }
  .marker circle.ring { fill: none; stroke-width: 0.18; opacity: 0; transition: opacity .15s ease; }
  .marker:hover circle.ring, .marker.active circle.ring { opacity: 1; }
  .marker circle.dot { stroke: var(--surface-1); stroke-width: 0.12; }

  .side-panel { background: var(--surface-2); border: 1px solid var(--border); border-radius: 12px; padding: 16px 18px; min-height: 300px; }
  .side-panel h2 { font-size: 15.5px; margin: 0 0 2px; }
  .side-panel .loc-meta { font-size: 12px; color: var(--text-muted); margin-bottom: 10px; }
  .type-pill { display: inline-flex; align-items: center; gap: 5px; font-size: 11px; font-weight: 700; padding: 3px 9px; border-radius: 999px; background: var(--surface-3); color: var(--text-secondary); margin-bottom: 10px; }
  .type-pill .chip-dot { width: 8px; height: 8px; }
  .side-panel .note { font-size: 13px; color: var(--text-secondary); line-height: 1.55; margin-bottom: 12px; }
  .risk-callout { border-left: 3px solid var(--warning); background: var(--warning-bg); border-radius: 6px; padding: 10px 12px; font-size: 12.5px; color: var(--text-primary); line-height: 1.5; }
  :root[data-theme="dark"] .risk-callout { color: var(--text-secondary); }
  .risk-callout b { display: block; margin-bottom: 3px; font-size: 12px; }
  .placeholder { color: var(--text-muted); font-size: 13px; line-height: 1.6; }

  .legend-block { margin-top: 18px; }
  .legend-block h3 { font-size: 11px; text-transform: uppercase; letter-spacing: .03em; color: var(--text-muted); margin: 0 0 8px; }
  .legend-row { display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--text-secondary); margin-bottom: 6px; }
  .legend-swatch { width: 13px; height: 13px; border-radius: 3px; flex: none; }

  .footer-note { margin-top: 20px; font-size: 11.5px; color: var(--text-muted); line-height: 1.6; }

  .intl-section { margin-top: 30px; padding-top: 22px; border-top: 1px solid var(--border); }
  .intl-head { display: flex; justify-content: space-between; align-items: baseline; gap: 12px; flex-wrap: wrap; margin-bottom: 4px; }
  .intl-head h2 { font-size: 17px; margin: 0; }
  .intl-scale { font-size: 12px; color: var(--text-muted); max-width: 420px; text-align: right; line-height: 1.5; }
  .intl-intro { font-size: 13px; color: var(--text-secondary); line-height: 1.55; margin: 6px 0 16px; max-width: 780px; }
  .intl-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
  .intl-card { background: var(--surface-2); border: 1px solid var(--border); border-radius: 12px; padding: 14px 16px; }
  .intl-card .intl-country { font-size: 14px; font-weight: 700; margin-bottom: 2px; }
  .intl-card .intl-city { font-size: 12px; color: var(--text-muted); margin-bottom: 8px; }
  .intl-card .intl-type { display: inline-block; font-size: 11px; font-weight: 700; background: var(--accent-soft); color: var(--accent); border-radius: 999px; padding: 3px 10px; margin-bottom: 10px; }
  .intl-card .intl-note { font-size: 12.5px; color: var(--text-secondary); line-height: 1.5; margin-bottom: 10px; }
  .intl-card .intl-risk { border-left: 3px solid var(--warning); background: var(--warning-bg); border-radius: 6px; padding: 8px 10px; font-size: 11.5px; color: var(--text-primary); line-height: 1.5; margin-bottom: 8px; }
  :root[data-theme="dark"] .intl-card .intl-risk { color: var(--text-secondary); }
  .intl-card .intl-source { font-size: 10.5px; color: var(--text-muted); }
  .intl-footnote { margin-top: 14px; font-size: 11.5px; color: var(--text-muted); line-height: 1.6; }

  @media (max-width: 880px) {
    .content { grid-template-columns: 1fr; }
    .intl-grid { grid-template-columns: 1fr; }
    .intl-head { flex-direction: column; }
    .intl-scale { text-align: left; }
  }
</style>
</head>
<body>
<div class="viz-root" id="vizRoot">
  <div class="wrap">
    <div class="top-bar">
      <div>
        <h1>UltraTech Cement — India Footprint & Regional Risk Map</h1>
        <p class="subtitle">Where the business actually sits on the ground — integrated plants (captive limestone + kiln), grinding units, and bulk/RMC distribution hubs — with a toggle to see which regions carry a specific operating risk. Companion to the Business Variable Framework and Process & Risk Map.</p>
      </div>
      <button class="theme-toggle" id="themeToggle">Dark mode</button>
    </div>

    <div class="controls">
      <div class="control-group">
        <span class="control-label">Show:</span>
        <label class="chip-toggle"><input type="checkbox" class="type-cb" value="integrated" checked><span class="chip-dot" style="background:#2a78d6"></span>Integrated plants</label>
        <label class="chip-toggle"><input type="checkbox" class="type-cb" value="grinding" checked><span class="chip-dot" style="background:#eb6834"></span>Grinding units</label>
        <label class="chip-toggle"><input type="checkbox" class="type-cb" value="hub" checked><span class="chip-dot" style="background:#1baf7a"></span>Bulk / RMC hubs</label>
      </div>
      <div class="control-group">
        <button class="risk-toggle-btn" id="riskToggle">Show regional risk overlay</button>
      </div>
    </div>

    <div class="content">
      <div class="map-panel">
        <svg class="mapsvg" id="mapSvg" viewBox="__VIEWBOX__" xmlns="http://www.w3.org/2000/svg"></svg>
      </div>
      <div class="side-panel" id="sidePanel">
        <div class="placeholder">Click any marker on the map to see the location's details and the regional risks that could affect it. Use the checkboxes above to filter by facility type, or turn on the risk overlay to see which states carry a specific operating risk (mining disputes, cyclone exposure, water stress, or pollution curbs).</div>
        <div class="legend-block">
          <h3>Facility type</h3>
          <div class="legend-row"><span class="legend-swatch" style="background:#2a78d6"></span>Integrated plant — has its own captive limestone quarry + kiln</div>
          <div class="legend-row"><span class="legend-swatch" style="background:#eb6834"></span>Grinding unit — finishes clinker into cement, closer to demand</div>
          <div class="legend-row"><span class="legend-swatch" style="background:#1baf7a"></span>Bulk terminal / RMC & distribution hub</div>
        </div>
        <div class="legend-block">
          <h3>Regional risk overlay (toggle above)</h3>
          <div class="legend-row"><span class="legend-swatch" style="background:#f3d9d0"></span>Mining / land & community risk</div>
          <div class="legend-row"><span class="legend-swatch" style="background:#d8e6f7"></span>Cyclone / coastal weather risk</div>
          <div class="legend-row"><span class="legend-swatch" style="background:#f6e6c8"></span>Water stress risk</div>
          <div class="legend-row"><span class="legend-swatch" style="background:#e6ded0"></span>Pollution-curb / GRAP risk</div>
        </div>
      </div>
    </div>

    <div class="footer-note">Plant locations are approximate (city/district-level, not exact GPS) and compiled from public company disclosures and industry sources — good enough to see the pattern, not for engineering use. A few sites marked "approx." still need location confirmation. Regional risk tags are illustrative starting points based on known regional characteristics (mining belts, coastlines, water-stress zones, NCR pollution rules) — treat as a research prompt, not a rated conclusion.</div>

    <div class="intl-section">
      <div class="intl-head">
        <h2>International Footprint</h2>
        <div class="intl-scale">__INTL_SCALE_NOTE__</div>
      </div>
      <p class="intl-intro">Outside India, UltraTech's presence is small and concentrated around the Gulf and Sri Lanka — a minority equity stake plus two wholly-owned grinding/packing plants, not a second manufacturing base on the scale of India.</p>
      <div class="intl-grid" id="intlGrid"></div>
      <div class="intl-footnote">__INTL_NOTE__</div>
    </div>
  </div>
</div>

<script>
const STATE_DATA = __STATE_DATA__;
const LOCATIONS = __LOCATIONS__;
const RISK_NOTES = __RISK_NOTES__;
const TYPE_META = __TYPE_META__;
const BOUNDS = __BOUNDS__;

function project(lon, lat) {
  const x = (lon - BOUNDS.minx) * BOUNDS.cos_lat;
  const y = (BOUNDS.maxy - lat);
  return [x, y];
}

const svg = document.getElementById("mapSvg");
const svgNS = "http://www.w3.org/2000/svg";

// state name -> risk tag(s) present among locations in that state (for overlay)
const stateRisk = {};
LOCATIONS.forEach(loc => {
  if (loc.risk) {
    stateRisk[loc.state] = stateRisk[loc.state] || new Set();
    stateRisk[loc.state].add(loc.risk);
  }
});

// draw states
const statesGroup = document.createElementNS(svgNS, "g");
statesGroup.setAttribute("id", "statesGroup");
STATE_DATA.states.forEach(s => {
  const p = document.createElementNS(svgNS, "path");
  p.setAttribute("d", s.path);
  p.setAttribute("class", "state-path");
  p.dataset.state = s.name;
  statesGroup.appendChild(p);
});
svg.appendChild(statesGroup);

// draw markers
const markersGroup = document.createElementNS(svgNS, "g");
markersGroup.setAttribute("id", "markersGroup");
LOCATIONS.forEach((loc, i) => {
  const [x, y] = project(loc.lon, loc.lat);
  const g = document.createElementNS(svgNS, "g");
  g.setAttribute("class", "marker");
  g.dataset.idx = i;
  g.dataset.type = loc.type;
  const color = TYPE_META[loc.type].color;

  const ring = document.createElementNS(svgNS, "circle");
  ring.setAttribute("class", "ring");
  ring.setAttribute("cx", x); ring.setAttribute("cy", y); ring.setAttribute("r", 0.55);
  ring.setAttribute("stroke", color);
  g.appendChild(ring);

  const dot = document.createElementNS(svgNS, "circle");
  dot.setAttribute("class", "dot");
  dot.setAttribute("cx", x); dot.setAttribute("cy", y); dot.setAttribute("r", 0.28);
  dot.setAttribute("fill", color);
  g.appendChild(dot);

  g.addEventListener("click", () => selectLocation(i));
  markersGroup.appendChild(g);
});
svg.appendChild(markersGroup);

const sidePanel = document.getElementById("sidePanel");
function selectLocation(i) {
  document.querySelectorAll(".marker").forEach(m => m.classList.remove("active"));
  document.querySelector(`.marker[data-idx="${i}"]`).classList.add("active");
  const loc = LOCATIONS[i];
  const meta = TYPE_META[loc.type];
  let riskHtml = "";
  if (loc.risk) {
    const r = RISK_NOTES[loc.risk];
    riskHtml = `<div class="risk-callout"><b>${r.label}</b>${r.detail}</div>`;
  }
  sidePanel.innerHTML = `
    <h2>${loc.name}</h2>
    <div class="loc-meta">${loc.city} · ${loc.state}</div>
    <div class="type-pill"><span class="chip-dot" style="background:${meta.color}"></span>${meta.label}</div>
    <div class="note">${loc.note}</div>
    ${riskHtml}
    <div class="legend-block">
      <h3>Facility type</h3>
      <div class="legend-row"><span class="legend-swatch" style="background:#2a78d6"></span>Integrated plant — captive limestone + kiln</div>
      <div class="legend-row"><span class="legend-swatch" style="background:#eb6834"></span>Grinding unit</div>
      <div class="legend-row"><span class="legend-swatch" style="background:#1baf7a"></span>Bulk terminal / RMC hub</div>
    </div>
  `;
}

// filters
function applyFilters() {
  const checked = new Set(Array.from(document.querySelectorAll(".type-cb:checked")).map(cb => cb.value));
  document.querySelectorAll(".marker").forEach(m => {
    m.style.display = checked.has(m.dataset.type) ? "" : "none";
  });
}
document.querySelectorAll(".type-cb").forEach(cb => cb.addEventListener("change", applyFilters));

// risk overlay toggle
let riskOn = false;
const riskBtn = document.getElementById("riskToggle");
riskBtn.addEventListener("click", () => {
  riskOn = !riskOn;
  riskBtn.classList.toggle("on", riskOn);
  riskBtn.textContent = riskOn ? "Hide regional risk overlay" : "Show regional risk overlay";
  document.querySelectorAll(".state-path").forEach(p => {
    p.className.baseVal = "state-path";
    if (riskOn && stateRisk[p.dataset.state]) {
      const tags = Array.from(stateRisk[p.dataset.state]);
      p.classList.add("risk-" + tags[0]);
    }
  });
});

// international cards
const INTL = __INTL__;
const intlGrid = document.getElementById("intlGrid");
INTL.forEach(c => {
  const div = document.createElement("div");
  div.className = "intl-card";
  div.innerHTML = `
    <div class="intl-country">${c.flag} ${c.country}</div>
    <div class="intl-city">${c.city}</div>
    <div class="intl-type">${c.type}</div>
    <div class="intl-note">${c.note}</div>
    <div class="intl-risk">${c.risk}</div>
    <div class="intl-source">Source: ${c.source}</div>
  `;
  intlGrid.appendChild(div);
});

// theme toggle
const themeToggle = document.getElementById("themeToggle");
const root = document.documentElement;
function applyThemeLabel() {
  const current = root.getAttribute("data-theme");
  themeToggle.textContent = current === "dark" ? "Light mode" : "Dark mode";
}
themeToggle.addEventListener("click", () => {
  const current = root.getAttribute("data-theme");
  root.setAttribute("data-theme", current === "dark" ? "light" : "dark");
  applyThemeLabel();
});
applyThemeLabel();
</script>
</body>
</html>
"""

html = html.replace("__VIEWBOX__", states_data["viewBox"])
html = html.replace("__STATE_DATA__", json.dumps(states_data))
html = html.replace("__LOCATIONS__", json.dumps(LOCATIONS))
html = html.replace("__RISK_NOTES__", json.dumps(RISK_NOTES))
html = html.replace("__TYPE_META__", json.dumps(TYPE_META))
html = html.replace("__BOUNDS__", json.dumps(bounds))
html = html.replace("__INTL__", json.dumps(INTL))
html = html.replace("__INTL_NOTE__", INTL_NOTE)
html = html.replace("__INTL_SCALE_NOTE__", INTL_SCALE_NOTE)

open("/home/claude/equity_research/ultratech_india_map.html", "w").write(html)
print("wrote html, size", len(html))
