import json

states_data = json.load(open("/home/claude/equity_research/india_states_paths.json"))
bounds = states_data["bounds"]

LOCATIONS = [
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
INTL_SCALE_NOTE = "Scale check: India domestic grey cement capacity alone crossed 200 MTPA in FY2025-26, while total consolidated (India + international) capacity has been reported around 205 MTPA in recent years — implying international operations are a small single-digit percentage of total capacity. (Exact current revenue/capacity split not yet researched — flagged for follow-up.)"

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UltraTech Cement — Business Overview</title>
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
    --good-bg:        #e5f7e5;
    --warning-bg:     #fff4dd;
    --critical-bg:    #fbe6e6;
  }
  @media (prefers-color-scheme: dark) {
    :root:where(:not([data-theme="light"])) .viz-root {
      color-scheme: dark;
      --surface-1: #1a1a19; --surface-2: #232322; --surface-3: #2c2c2a; --border: #3a3a37;
      --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #8f8d84;
      --accent: #3987e5; --accent-soft: #17263a; --map-fill: #2a2a27; --map-stroke: #45443f;
      --good: #0ca30c; --warning: #fab219; --critical: #e66767;
      --good-bg: #123312; --warning-bg: #3a2c0e; --critical-bg: #3a1717;
    }
  }
  :root[data-theme="dark"] .viz-root {
    color-scheme: dark;
    --surface-1: #1a1a19; --surface-2: #232322; --surface-3: #2c2c2a; --border: #3a3a37;
    --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #8f8d84;
    --accent: #3987e5; --accent-soft: #17263a; --map-fill: #2a2a27; --map-stroke: #45443f;
    --good: #0ca30c; --warning: #fab219; --critical: #e66767;
    --good-bg: #123312; --warning-bg: #3a2c0e; --critical-bg: #3a1717;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif; background: var(--surface-1); color: var(--text-primary); }
  .viz-root { background: var(--surface-1); min-height: 100vh; padding: 26px 24px 50px; }
  .wrap { max-width: 1200px; margin: 0 auto; }
  .top-bar { display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; }
  h1 { font-size: 21px; margin: 0 0 4px; }
  .subtitle { color: var(--text-secondary); font-size: 13.5px; margin: 0 0 18px; max-width: 780px; line-height: 1.5; }
  .theme-toggle { background: var(--surface-2); border: 1px solid var(--border); color: var(--text-secondary); border-radius: 8px; padding: 6px 12px; font-size: 12px; cursor: pointer; white-space: nowrap; }
  .theme-toggle:hover { background: var(--surface-3); }

  /* Tabs */
  .tab-bar { display: flex; gap: 6px; margin-bottom: 20px; border-bottom: 1px solid var(--border); }
  .tab-btn { background: none; border: none; border-bottom: 2px solid transparent; color: var(--text-muted); font-size: 13.5px; font-weight: 600; padding: 10px 4px; margin-right: 22px; cursor: pointer; font-family: inherit; }
  .tab-btn:hover { color: var(--text-primary); }
  .tab-btn.active { color: var(--accent); border-bottom-color: var(--accent); }
  .tab-panel { display: none; }
  .tab-panel.active { display: block; }

  /* Legend / badges (process tab) */
  .legend { display: flex; gap: 18px; flex-wrap: wrap; margin-bottom: 24px; font-size: 12.5px; color: var(--text-secondary); align-items: center; }
  .legend-item { display: flex; align-items: center; gap: 6px; }
  .dot { width: 10px; height: 10px; border-radius: 50%; flex: none; }
  .dot.good { background: var(--good); }
  .dot.warning { background: var(--warning); }
  .dot.critical { background: var(--critical); }
  .legend-hint { color: var(--text-muted); }

  .flow { display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-bottom: 8px; }
  .arrow-row { display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-bottom: 10px; }
  .stage {
    display: block; text-decoration: none;
    background: var(--surface-2); border: 1.5px solid var(--border); border-radius: 10px; padding: 14px 12px;
    cursor: pointer; text-align: left; transition: border-color .15s ease, transform .1s ease, box-shadow .15s ease;
    position: relative; font-family: inherit; color: var(--text-primary);
  }
  .stage:hover { border-color: var(--accent); transform: translateY(-2px); box-shadow: 0 4px 14px rgba(0,0,0,.08); }
  .stage.active { border-color: var(--accent); background: var(--accent-soft); }
  .stage .stage-num { font-size: 10.5px; color: var(--text-muted); font-weight: 600; letter-spacing: .04em; text-transform: uppercase; }
  .stage .stage-title { font-size: 13.5px; font-weight: 700; margin: 4px 0 8px; line-height: 1.25; min-height: 34px; }
  .stage .risk-badges { display: flex; gap: 4px; flex-wrap: wrap; }
  .stage .stage-cta { font-size: 11px; font-weight: 600; color: var(--accent); margin-top: 10px; opacity: 0; transition: opacity .15s ease; }
  .stage:hover .stage-cta { opacity: 1; }
  .badge { display: inline-flex; align-items: center; gap: 3px; font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 5px; line-height: 1.6; }
  .badge.good { color: var(--good); background: var(--good-bg); }
  .badge.warning { color: #a8720c; background: var(--warning-bg); }
  .badge.critical { color: var(--critical); background: var(--critical-bg); }
  .badge svg { width: 9px; height: 9px; }
  .connector { display: flex; align-items: center; justify-content: center; color: var(--text-muted); font-size: 16px; }

  .detail { background: var(--surface-2); border: 1.5px solid var(--accent); border-radius: 12px; padding: 20px 22px; margin-top: 18px; }
  .detail-head { display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; margin-bottom: 4px; }
  .detail-head h2 { font-size: 17px; margin: 0; }
  .detail-summary { color: var(--text-secondary); font-size: 13px; margin: 4px 0 16px; line-height: 1.55; }
  .steps { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px; }
  .step-chip { background: var(--surface-3); border: 1px solid var(--border); border-radius: 999px; padding: 4px 10px; font-size: 11.5px; color: var(--text-secondary); }
  table.risk-table { width: 100%; border-collapse: collapse; font-size: 12.5px; }
  table.risk-table th { text-align: left; font-size: 10.5px; text-transform: uppercase; letter-spacing: .03em; color: var(--text-muted); font-weight: 700; padding: 6px 10px; border-bottom: 1px solid var(--border); }
  table.risk-table td { padding: 9px 10px; border-bottom: 1px solid var(--border); vertical-align: top; color: var(--text-primary); }
  table.risk-table tr:last-child td { border-bottom: none; }
  .rt-variable { font-weight: 700; white-space: nowrap; }
  .rt-source { color: var(--text-muted); font-size: 11px; }
  .close-hint { font-size: 11px; color: var(--text-muted); cursor: pointer; }
  .close-hint:hover { color: var(--text-secondary); }
  .crosscut { margin-top: 22px; padding-top: 18px; border-top: 1px dashed var(--border); }
  .crosscut h3 { font-size: 13px; text-transform: uppercase; letter-spacing: .03em; color: var(--text-muted); margin: 0 0 10px; }
  .cc-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  .cc-card { background: var(--surface-2); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; }
  .cc-card .cc-title { font-size: 12.5px; font-weight: 700; margin-bottom: 4px; }
  .cc-card .cc-body { font-size: 12px; color: var(--text-secondary); line-height: 1.5; }

  /* Map tab */
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

  @media (max-width: 900px) {
    .flow, .arrow-row { grid-template-columns: repeat(3, 1fr); }
    .arrow-row .connector:nth-child(3n) { display: none; }
    .cc-grid { grid-template-columns: 1fr; }
  }
  @media (max-width: 880px) {
    .content { grid-template-columns: 1fr; }
    .intl-grid { grid-template-columns: 1fr; }
    .intl-head { flex-direction: column; }
    .intl-scale { text-align: left; }
  }
  @media (max-width: 560px) {
    .flow, .arrow-row { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="viz-root" id="vizRoot">
  <div class="wrap">
    <div class="top-bar">
      <div>
        <h1>UltraTech Cement — Business Overview</h1>
        <p class="subtitle">Two views of the same business: how it turns raw materials into revenue, and where it physically operates (India + international) with the regional risks that follow from that. Companion to the Business Variable Framework workbook.</p>
      </div>
      <button class="theme-toggle" id="themeToggle">Dark mode</button>
    </div>

    <div class="tab-bar">
      <button class="tab-btn active" id="tabBtnProcess">Process & Risk Map</button>
      <button class="tab-btn" id="tabBtnMap">India & International Footprint</button>
    </div>

    <!-- ===================== TAB 1: PROCESS ===================== -->
    <div class="tab-panel active" id="tabProcess">
      <p class="intl-intro" style="margin-top:0">Click any step below to open its full detail page — deeper explanation, the complete risk table, and the plant/facility locations on the map that matter for that specific step.</p>
      <div class="legend">
        <span class="legend-hint">Risk / impact level:</span>
        <span class="legend-item"><span class="dot good"></span>Low</span>
        <span class="legend-item"><span class="dot warning"></span>Medium</span>
        <span class="legend-item"><span class="dot critical"></span>High</span>
      </div>
      <div class="flow" id="flowRow"></div>
      <div class="arrow-row" id="arrowRow"></div>
      <div class="footer-note">Companion to Business_Variable_Framework.xlsx. Ratings: Low = well-managed / low exposure, Medium = matters but has some buffer, High = could meaningfully hurt the business if it goes wrong.</div>
    </div>

    <!-- ===================== TAB 2: MAP ===================== -->
    <div class="tab-panel" id="tabMap">
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
          <div class="placeholder">Click any marker on the map to see the location's details and the regional risks that could affect it. Use the checkboxes above to filter by facility type, or turn on the risk overlay to see which states carry a specific operating risk.</div>
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

      <div class="footer-note">Plant locations are approximate (city/district-level, not exact GPS). A few sites marked "approx." still need location confirmation. Regional risk tags are illustrative starting points, not verified ratings.</div>

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
</div>

<script>
/* ============ Shared: theme toggle ============ */
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

/* ============ Shared: tab switching ============ */
const tabBtnProcess = document.getElementById("tabBtnProcess");
const tabBtnMap = document.getElementById("tabBtnMap");
const tabProcess = document.getElementById("tabProcess");
const tabMap = document.getElementById("tabMap");
let mapInitialized = false;

function showTab(which) {
  tabBtnProcess.classList.toggle("active", which === "process");
  tabBtnMap.classList.toggle("active", which === "map");
  tabProcess.classList.toggle("active", which === "process");
  tabMap.classList.toggle("active", which === "map");
  if (which === "map" && !mapInitialized) {
    initMap();
    mapInitialized = true;
  }
}
tabBtnProcess.addEventListener("click", () => showTab("process"));
tabBtnMap.addEventListener("click", () => showTab("map"));

/* ============ TAB 1: Process & Risk data/render ============ */
const STAGES = [
  {
    id: "procure-raw", url: "step-01-procure-raw.html", num: "01", title: "Procure raw materials", topRisk: "warning",
    summary: "Limestone, clay, silica and gypsum are mined or sourced near each plant — the first link in the chain and the one that decides where a plant can even be built.",
    steps: ["Limestone quarrying", "Clay / silica sourcing", "Gypsum sourcing", "Quality testing of ore"],
    risks: [
      { variable: "Source location", level: "warning", text: "Materials sourced near plant sites across India (e.g. Chhattisgarh limestone) — regional concentration means local disruption can hit supply.", source: "Zerodha Varsity" },
      { variable: "Captive vs. open market", level: "good", text: "UltraTech owns captive limestone quarries built next to its plants — a real cost & supply-security advantage over smaller players.", source: "Zerodha Varsity" },
      { variable: "Supplier concentration", level: "warning", text: "Largely self-supplied for limestone; clay/silica/gypsum still involve regional suppliers.", source: "Zerodha Varsity" },
      { variable: "Regulatory: mining leases", level: "warning", text: "Requires state-level mining leases and environmental clearances — can be delayed, contested, or revoked.", source: "Zerodha Varsity" },
    ],
  },
  {
    id: "procure-fuel", url: "step-02-procure-fuel.html", num: "02", title: "Procure fuel & power", topRisk: "critical",
    summary: "Cement kilns need enormous heat (~1450°C) — coal and petcoke are burned to get there, and power runs the grinding and crushing equipment. This is the single biggest cost swing factor in the business.",
    steps: ["Coal / petcoke sourcing", "Captive coal linkage", "Grid + captive power", "Renewable / waste-heat capture"],
    risks: [
      { variable: "Input price volatility", level: "critical", text: "Coal/petcoke prices are volatile and the biggest swing factor in cement costs — roughly 160kg of coal per tonne of cement produced.", source: "Safal Niveshak" },
      { variable: "Captive vs. open market", level: "good", text: "UltraTech holds captive coal mine linkages, partially insulating it from open-market price spikes (unlike many smaller peers).", source: "Zerodha Varsity" },
      { variable: "Substitutability", level: "warning", text: "Few large-scale fuel substitutes exist yet; UltraTech is investing in waste heat recovery + renewables to cover 25-30% of energy needs over time.", source: "Zerodha Varsity" },
      { variable: "Trade policy exposure", level: "warning", text: "A portion of coal is imported, so import duties and global coal prices matter directly to cost.", source: "Not yet researched — flagged for follow-up" },
    ],
  },
  {
    id: "manufacture", url: "step-03-manufacture.html", num: "03", title: "Manufacture (kiln process)", topRisk: "critical",
    summary: "Raw materials are crushed and ground into 'raw meal', preheated, then burned in a kiln to form clinker — the core intermediate product — which is cooled and ground with gypsum into cement.",
    steps: ["Crushing", "Raw meal grinding", "Preheating / precalcining", "Kiln burning → clinker (~1450°C)", "Cooling", "Cement grinding (clinker + gypsum)"],
    risks: [
      { variable: "Environmental / ESG exposure", level: "critical", text: "Cement manufacturing is carbon- and energy-intensive; tightening emissions norms are a probable future cost driver for kiln operations.", source: "Zerodha Varsity" },
      { variable: "Fixed vs. variable costs", level: "warning", text: "Heavy fixed-cost base (plant, kiln) plus variable fuel/power costs — capacity utilization strongly drives per-unit profitability.", source: "Framework analysis" },
      { variable: "Capital intensity", level: "warning", text: "New capacity costs roughly ₹7,200/tonne (2013 figure, higher today); UltraTech is investing ~₹16,000 crore to expand to 242.5 MTPA by FY2027-28.", source: "The Strategy Story" },
      { variable: "Returns trend", level: "critical", text: "Industry-wide, returns on new cement capacity have fallen over time (IRR ~17% in 2008 to ~9% in 2013) — a red flag for future capacity decisions.", source: "Safal Niveshak" },
    ],
  },
  {
    id: "package-qc", url: "step-04-package-qc.html", num: "04", title: "Package & quality-check", topRisk: "good",
    summary: "Finished cement is tested in-lab against strength/quality standards, then packed into bags or loaded in bulk for dispatch.",
    steps: ["Lab quality testing", "Bagging / bulk loading", "Storage (silos)"],
    risks: [
      { variable: "Process maturity", level: "good", text: "Packaging and QC are standardized, well-understood processes across the industry — not a major source of business risk.", source: "Framework analysis" },
      { variable: "Cement shelf-life", level: "warning", text: "Cement has roughly a 90-day usable shelf life, which is why grinding/packing plants are kept close to regional demand rather than stockpiled centrally.", source: "Zerodha Varsity" },
    ],
  },
  {
    id: "distribute", url: "step-05-distribute.html", num: "05", title: "Distribute & transport", topRisk: "critical",
    summary: "Because cement is heavy and low-value-per-kg, freight cost dominates. Plants effectively serve only a 150-300 km radius before transport eats the margin — this is why cement is a fundamentally regional business.",
    steps: ["Road / rail dispatch", "Regional warehousing", "RMC plant delivery", "Last-mile to dealer / site"],
    risks: [
      { variable: "Logistics cost share", level: "critical", text: "Freight/transportation is roughly 20-25% of sales industry-wide — often bigger than net profit margin — making location and network the real competitive edge.", source: "Safal Niveshak" },
      { variable: "Distance to market", level: "warning", text: "Plants typically serve customers within 150-300 km; UltraTech's scale gives it coverage of 90%+ of India's talukas.", source: "Safal Niveshak" },
      { variable: "Regional concentration risk", level: "good", text: "UltraTech is diversified across regions (plus UAE, Bahrain, Sri Lanka) rather than concentrated in one state.", source: "The Strategy Story" },
    ],
  },
  {
    id: "sell", url: "step-06-sell.html", num: "06", title: "Sell to customers", topRisk: "warning",
    summary: "Cement reaches builders and homeowners mainly through a vast dealer network, plus direct sales to large contractors and infrastructure projects, and a growing retail 'Building Solutions' channel.",
    steps: ["Dealer / channel-partner network", "B2B: contractors & infra projects", "B2C: individual home-builders", "Building Solutions retail outlets"],
    risks: [
      { variable: "Customer concentration", level: "good", text: "Very fragmented — 1.5+ lakh channel partners and ~30,000 delivery destinations — so no single customer has real bargaining power.", source: "The Strategy Story" },
      { variable: "Pricing power", level: "warning", text: "Limited industry-wide — transparent local pricing tends to trigger price wars when regional capacity utilization is low.", source: "Safal Niveshak" },
      { variable: "Demand driver", level: "warning", text: "Sales track housing, infrastructure and industrial construction activity — cyclical with GDP (~1.2x) and seasonally weaker in monsoon.", source: "Safal Niveshak" },
      { variable: "Market concentration", level: "good", text: "Consolidated industry — top 3-4 players hold roughly a third of capacity, with UltraTech the largest — supports more rational competition than a fragmented market.", source: "Safal Niveshak" },
    ],
  },
];

const CROSSCUT = [
  { title: "Ownership & governance", body: "Part of the Aditya Birla Group — an established Indian promoter conglomerate. Low risk from an ownership-stability standpoint." },
  { title: "Financial leverage", body: "Not yet researched — debt/EBITDA or debt/equity needs to be pulled from the balance sheet before this can be rated." },
  { title: "Regulatory disputes", body: "Not yet researched — check for pending mining or environmental litigation, including reported community concerns around mining in Chhattisgarh." },
];

function riskIcon(level) {
  if (level === "good") return '<svg viewBox="0 0 16 16" fill="none"><path d="M3 8.5L6.5 12L13 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  if (level === "warning") return '<svg viewBox="0 0 16 16" fill="none"><path d="M8 2L14.5 13H1.5L8 2Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M8 6.5V9.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="8" cy="11.3" r="0.9" fill="currentColor"/></svg>';
  return '<svg viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.6"/><path d="M8 5V8.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="8" cy="10.8" r="0.9" fill="currentColor"/></svg>';
}
function riskLabel(level) { return level === "good" ? "Low" : level === "warning" ? "Medium" : "High"; }

const flowRow = document.getElementById("flowRow");
const arrowRow = document.getElementById("arrowRow");

STAGES.forEach((s, i) => {
  const btn = document.createElement("a");
  btn.className = "stage";
  btn.id = "stage-" + s.id;
  btn.href = s.url;
  btn.innerHTML = `
    <div class="stage-num">Step ${s.num}</div>
    <div class="stage-title">${s.title}</div>
    <div class="risk-badges">
      ${[...new Set(s.risks.map(r => r.level))].sort((a,b)=>({critical:0,warning:1,good:2}[a]-{critical:0,warning:1,good:2}[b])).map(lvl => `<span class="badge ${lvl}">${riskIcon(lvl)}${riskLabel(lvl)}</span>`).join("")}
    </div>
    <div class="stage-cta">Open step page →</div>
  `;
  flowRow.appendChild(btn);

  if (i < STAGES.length - 1) {
    const conn = document.createElement("div");
    conn.className = "connector";
    conn.textContent = "→";
    arrowRow.appendChild(conn);
  } else {
    arrowRow.appendChild(document.createElement("div"));
  }
});

/* ============ TAB 2: Map data/render (lazy-initialized on first view) ============ */
const STATE_DATA = __STATE_DATA__;
const LOCATIONS = __LOCATIONS__;
const RISK_NOTES = __RISK_NOTES__;
const TYPE_META = __TYPE_META__;
const BOUNDS = __BOUNDS__;
const INTL = __INTL__;

function project(lon, lat) {
  const x = (lon - BOUNDS.minx) * BOUNDS.cos_lat;
  const y = (BOUNDS.maxy - lat);
  return [x, y];
}

function initMap() {
  const svg = document.getElementById("mapSvg");
  const svgNS = "http://www.w3.org/2000/svg";

  const stateRisk = {};
  LOCATIONS.forEach(loc => {
    if (loc.risk) {
      stateRisk[loc.state] = stateRisk[loc.state] || new Set();
      stateRisk[loc.state].add(loc.risk);
    }
  });

  const statesGroup = document.createElementNS(svgNS, "g");
  STATE_DATA.states.forEach(s => {
    const p = document.createElementNS(svgNS, "path");
    p.setAttribute("d", s.path);
    p.setAttribute("class", "state-path");
    p.dataset.state = s.name;
    statesGroup.appendChild(p);
  });
  svg.appendChild(statesGroup);

  const markersGroup = document.createElementNS(svgNS, "g");
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
  window.selectLocation = function(i) {
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
  };

  function applyFilters() {
    const checked = new Set(Array.from(document.querySelectorAll(".type-cb:checked")).map(cb => cb.value));
    document.querySelectorAll(".marker").forEach(m => {
      m.style.display = checked.has(m.dataset.type) ? "" : "none";
    });
  }
  document.querySelectorAll(".type-cb").forEach(cb => cb.addEventListener("change", applyFilters));

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
}

if (window.location.hash === "#map") showTab("map");
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

open("/home/claude/equity_research/ultratech_overview.html", "w").write(html)
print("wrote html, size", len(html))
