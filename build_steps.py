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

CROSSCUT = [
    {"title": "Ownership & governance", "body": "Part of the Aditya Birla Group — an established Indian promoter conglomerate. Low risk from an ownership-stability standpoint."},
    {"title": "Financial leverage", "body": "Not yet researched — debt/EBITDA or debt/equity needs to be pulled from the balance sheet before this can be rated."},
    {"title": "Regulatory disputes", "body": "Not yet researched — check for pending mining or environmental litigation, including reported community concerns around mining in Chhattisgarh."},
]

STAGES = [
    {
        "id": "procure-raw", "url": "step-01-procure-raw.html", "num": "01", "title": "Procure raw materials", "topRisk": "warning",
        "summary": "Limestone, clay, silica and gypsum are mined or sourced near each plant — the first link in the chain and the one that decides where a plant can even be built.",
        "steps": ["Limestone quarrying", "Clay / silica sourcing", "Gypsum sourcing", "Quality testing of ore"],
        "risks": [
            {"variable": "Source location", "level": "warning", "text": "Materials sourced near plant sites across India (e.g. Chhattisgarh limestone) — regional concentration means local disruption can hit supply.", "source": "Zerodha Varsity"},
            {"variable": "Captive vs. open market", "level": "good", "text": "UltraTech owns captive limestone quarries built next to its plants — a real cost & supply-security advantage over smaller players.", "source": "Zerodha Varsity"},
            {"variable": "Supplier concentration", "level": "warning", "text": "Largely self-supplied for limestone; clay/silica/gypsum still involve regional suppliers.", "source": "Zerodha Varsity"},
            {"variable": "Regulatory: mining leases", "level": "warning", "text": "Requires state-level mining leases and environmental clearances — can be delayed, contested, or revoked.", "source": "Zerodha Varsity"},
        ],
        "deep_dive": [
            "UltraTech's integrated plants are built next to their own limestone quarries — the industry's standard 'mine-mouth' model for controlling the single largest physical input to cement by weight. Owning the quarry means the company isn't paying a market price for its main raw material and isn't dependent on a third-party supplier's output decisions.",
            "The trade-off is permanence: a quarry can't be relocated, so a plant's location and its mine's location are really the same decision, made once for decades. Clay, silica and gypsum are smaller inputs by volume but are still typically sourced regionally, to keep freight costs down before the material even reaches the kiln.",
        ],
        "open_question": "How many years of reserve life remain at UltraTech's key quarries, and how much of future capacity expansion depends on securing new mining leases versus expanding at existing sites? Not yet researched.",
        "map_types": ["integrated"],
        "map_caption": "Every integrated plant below sits next to its own captive limestone quarry — this is literally where raw material procurement happens. Grinding units and bulk terminals are hidden by default since they don't do primary raw-material sourcing.",
    },
    {
        "id": "procure-fuel", "url": "step-02-procure-fuel.html", "num": "02", "title": "Procure fuel & power", "topRisk": "critical",
        "summary": "Cement kilns need enormous heat (~1450°C) — coal and petcoke are burned to get there, and power runs the grinding and crushing equipment. This is the single biggest cost swing factor in the business.",
        "steps": ["Coal / petcoke sourcing", "Captive coal linkage", "Grid + captive power", "Renewable / waste-heat capture"],
        "risks": [
            {"variable": "Input price volatility", "level": "critical", "text": "Coal/petcoke prices are volatile and the biggest swing factor in cement costs — roughly 160kg of coal per tonne of cement produced.", "source": "Safal Niveshak"},
            {"variable": "Captive vs. open market", "level": "good", "text": "UltraTech holds captive coal mine linkages, partially insulating it from open-market price spikes (unlike many smaller peers).", "source": "Zerodha Varsity"},
            {"variable": "Substitutability", "level": "warning", "text": "Few large-scale fuel substitutes exist yet; UltraTech is investing in waste heat recovery + renewables to cover 25-30% of energy needs over time.", "source": "Zerodha Varsity"},
            {"variable": "Trade policy exposure", "level": "warning", "text": "A portion of coal is imported, so import duties and global coal prices matter directly to cost.", "source": "Not yet researched — flagged for follow-up"},
        ],
        "deep_dive": [
            "Where raw materials are heavy but relatively cheap, fuel is the opposite: needed in smaller physical quantity but far more volatile in price and far more consequential for margins. A cement kiln runs at extreme, continuous temperature, so any interruption to fuel supply doesn't just raise costs — it can force a costly kiln shutdown and restart.",
            "UltraTech's captive coal linkages function like insurance against open-market price spikes, but the industry-wide push into waste heat recovery and renewables is really an attempt to reduce fuel dependence altogether rather than just hedge it — a structural response to a cost line that has proven hard to control any other way.",
        ],
        "open_question": "What share of UltraTech's kiln energy currently comes from linkage coal vs. imported coal/petcoke vs. renewables/waste heat, and how has that mix shifted over the last five years? Not yet researched.",
        "map_types": ["integrated"],
        "map_caption": "Fuel and captive power are tied to the same integrated plants shown for raw materials — the kiln that burns the fuel sits at the same site as the quarry.",
    },
    {
        "id": "manufacture", "url": "step-03-manufacture.html", "num": "03", "title": "Manufacture (kiln process)", "topRisk": "critical",
        "summary": "Raw materials are crushed and ground into 'raw meal', preheated, then burned in a kiln to form clinker — the core intermediate product — which is cooled and ground with gypsum into cement.",
        "steps": ["Crushing", "Raw meal grinding", "Preheating / precalcining", "Kiln burning → clinker (~1450°C)", "Cooling", "Cement grinding (clinker + gypsum)"],
        "risks": [
            {"variable": "Environmental / ESG exposure", "level": "critical", "text": "Cement manufacturing is carbon- and energy-intensive; tightening emissions norms are a probable future cost driver for kiln operations.", "source": "Zerodha Varsity"},
            {"variable": "Fixed vs. variable costs", "level": "warning", "text": "Heavy fixed-cost base (plant, kiln) plus variable fuel/power costs — capacity utilization strongly drives per-unit profitability.", "source": "Framework analysis"},
            {"variable": "Capital intensity", "level": "warning", "text": "New capacity costs roughly ₹7,200/tonne (2013 figure, higher today); UltraTech is investing ~₹16,000 crore to expand to 242.5 MTPA by FY2027-28.", "source": "The Strategy Story"},
            {"variable": "Returns trend", "level": "critical", "text": "Industry-wide, returns on new cement capacity have fallen over time (IRR ~17% in 2008 to ~9% in 2013) — a red flag for future capacity decisions.", "source": "Safal Niveshak"},
        ],
        "deep_dive": [
            "The kiln is the heart of the business and its biggest fixed asset — a single integrated line represents a large share of the capital UltraTech deploys per tonne of capacity. Because fixed costs here are so large, a plant's profitability is extremely sensitive to how much of its rated capacity it actually uses: a kiln running at 60% utilization loses money in a way a kiln at 90% does not, even though raw material and fuel cost per tonne barely change.",
            "This is also where environmental exposure concentrates. Cement kilns are among the more carbon-intensive industrial processes there is, so future emissions regulation is fundamentally a manufacturing-stage risk more than a sales-stage one — it shows up as a cost of running the kiln, long before it ever touches a customer.",
        ],
        "open_question": "What is UltraTech's current average capacity utilization across its plants, and how does it compare to peers like Ambuja/ACC and Shree Cement? Not yet researched.",
        "map_types": ["integrated"],
        "map_caption": "Manufacturing happens at the integrated plants — the only sites with a kiln. Grinding units further downstream finish clinker made here into cement, but don't run the kiln process itself.",
    },
    {
        "id": "package-qc", "url": "step-04-package-qc.html", "num": "04", "title": "Package & quality-check", "topRisk": "good",
        "summary": "Finished cement is tested in-lab against strength/quality standards, then packed into bags or loaded in bulk for dispatch.",
        "steps": ["Lab quality testing", "Bagging / bulk loading", "Storage (silos)"],
        "risks": [
            {"variable": "Process maturity", "level": "good", "text": "Packaging and QC are standardized, well-understood processes across the industry — not a major source of business risk.", "source": "Framework analysis"},
            {"variable": "Cement shelf-life", "level": "warning", "text": "Cement has roughly a 90-day usable shelf life, which is why grinding/packing plants are kept close to regional demand rather than stockpiled centrally.", "source": "Zerodha Varsity"},
        ],
        "deep_dive": [
            "Packaging and quality testing are the least differentiated, least risky part of the chain — every credible cement producer runs broadly the same lab tests and bagging process, so this step is more about operational discipline than competitive advantage.",
            "The one real constraint it imposes on the rest of the business is cement's roughly 90-day shelf life: because finished cement can't be stockpiled indefinitely, packaging capacity has to be sized and located close to where the cement will actually sell. That's a big part of why grinding/packing units get built near demand centers rather than near raw material sources — it's this step's requirement working backward on the network design.",
        ],
        "open_question": None,
        "map_types": ["integrated", "grinding"],
        "map_caption": "Both integrated plants and grinding units package and quality-check their own output — shown together here since packaging happens at every manufacturing site, not just one type.",
    },
    {
        "id": "distribute", "url": "step-05-distribute.html", "num": "05", "title": "Distribute & transport", "topRisk": "critical",
        "summary": "Because cement is heavy and low-value-per-kg, freight cost dominates. Plants effectively serve only a 150-300 km radius before transport eats the margin — this is why cement is a fundamentally regional business.",
        "steps": ["Road / rail dispatch", "Regional warehousing", "RMC plant delivery", "Last-mile to dealer / site"],
        "risks": [
            {"variable": "Logistics cost share", "level": "critical", "text": "Freight/transportation is roughly 20-25% of sales industry-wide — often bigger than net profit margin — making location and network the real competitive edge.", "source": "Safal Niveshak"},
            {"variable": "Distance to market", "level": "warning", "text": "Plants typically serve customers within 150-300 km; UltraTech's scale gives it coverage of 90%+ of India's talukas.", "source": "Safal Niveshak"},
            {"variable": "Regional concentration risk", "level": "good", "text": "UltraTech is diversified across regions (plus UAE, Bahrain, Sri Lanka) rather than concentrated in one state.", "source": "The Strategy Story"},
        ],
        "deep_dive": [
            "This is arguably the step that defines cement as an industry: unlike software or pharma, a cement company's competitiveness is set as much by where its plants sit relative to its customers as by anything happening inside the plant. Freight cost is large enough, relative to the product's value, that a well-located regional plant can beat a more efficient but farther-away plant on delivered price.",
            "UltraTech's scale advantage shows up here as much as in manufacturing — a bigger network of plants, grinding units and bulk terminals means more of the country falls inside someone's economical delivery radius, which is a big part of why the company can claim coverage of over 90% of India's talukas.",
        ],
        "open_question": None,
        "map_types": ["hub", "grinding"],
        "map_caption": "Bulk terminals/RMC hubs and grinding units are the front line of distribution — closest to customers and most sensitive to freight economics. Integrated plants are hidden by default; they're the origin point, not the delivery network.",
    },
    {
        "id": "sell", "url": "step-06-sell.html", "num": "06", "title": "Sell to customers", "topRisk": "warning",
        "summary": "Cement reaches builders and homeowners mainly through a vast dealer network, plus direct sales to large contractors and infrastructure projects, and a growing retail 'Building Solutions' channel.",
        "steps": ["Dealer / channel-partner network", "B2B: contractors & infra projects", "B2C: individual home-builders", "Building Solutions retail outlets"],
        "risks": [
            {"variable": "Customer concentration", "level": "good", "text": "Very fragmented — 1.5+ lakh channel partners and ~30,000 delivery destinations — so no single customer has real bargaining power.", "source": "The Strategy Story"},
            {"variable": "Pricing power", "level": "warning", "text": "Limited industry-wide — transparent local pricing tends to trigger price wars when regional capacity utilization is low.", "source": "Safal Niveshak"},
            {"variable": "Demand driver", "level": "warning", "text": "Sales track housing, infrastructure and industrial construction activity — cyclical with GDP (~1.2x) and seasonally weaker in monsoon.", "source": "Safal Niveshak"},
            {"variable": "Market concentration", "level": "good", "text": "Consolidated industry — top 3-4 players hold roughly a third of capacity, with UltraTech the largest — supports more rational competition than a fragmented market.", "source": "Safal Niveshak"},
        ],
        "deep_dive": [
            "The 'sale' itself is less a single event and more the result of everything upstream. A fragmented dealer network means no single customer can squeeze UltraTech on price — but it also means the company can't just decide to raise prices either. Local market conditions, mainly how much unused capacity nearby competitors have, set the real ceiling.",
            "The 'Building Solutions' retail push is UltraTech trying to move part of its business away from being a pure commodity seller, where price is everything, toward a branded, value-added relationship with the end customer — the same logic that pushes any commodity business toward downstream, higher-margin products when it can.",
        ],
        "open_question": None,
        "map_types": ["hub", "grinding"],
        "map_caption": "Customer-facing sales run through the same distribution network — grinding units and bulk/RMC hubs closest to demand — shown here again from the selling side of the same physical footprint.",
    },
]

STEP_URLS = [s["url"] for s in STAGES]

SHARED_CSS = r"""
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
  .viz-root { background: var(--surface-1); min-height: 100vh; padding: 26px 24px 60px; }
  .wrap { max-width: 1200px; margin: 0 auto; }
  .top-bar { display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; }
  h1 { font-size: 20px; margin: 0 0 4px; }
  .subtitle { color: var(--text-secondary); font-size: 13.5px; margin: 0 0 4px; max-width: 780px; line-height: 1.5; }
  .breadcrumb { font-size: 12px; color: var(--text-muted); margin-bottom: 14px; }
  .breadcrumb a { color: var(--accent); text-decoration: none; }
  .breadcrumb a:hover { text-decoration: underline; }
  .theme-toggle { background: var(--surface-2); border: 1px solid var(--border); color: var(--text-secondary); border-radius: 8px; padding: 6px 12px; font-size: 12px; cursor: pointer; white-space: nowrap; }
  .theme-toggle:hover { background: var(--surface-3); }

  /* step pill nav */
  .step-nav { display: flex; gap: 8px; flex-wrap: wrap; margin: 16px 0 26px; }
  .step-pill {
    display: flex; align-items: center; gap: 7px; text-decoration: none;
    background: var(--surface-2); border: 1.5px solid var(--border); border-radius: 999px;
    padding: 7px 13px 7px 9px; font-size: 12px; color: var(--text-secondary); font-weight: 600;
    transition: border-color .15s ease;
  }
  .step-pill:hover { border-color: var(--accent); }
  .step-pill.current { border-color: var(--accent); background: var(--accent-soft); color: var(--accent); }
  .step-pill .num-badge {
    width: 18px; height: 18px; border-radius: 50%; background: var(--surface-3); color: var(--text-muted);
    display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700; flex: none;
  }
  .step-pill.current .num-badge { background: var(--accent); color: #fff; }

  h2.section-title { font-size: 16px; margin: 34px 0 10px; padding-top: 20px; border-top: 1px solid var(--border); }
  h2.section-title:first-of-type { padding-top: 0; border-top: none; margin-top: 6px; }

  .lede { font-size: 14.5px; color: var(--text-secondary); line-height: 1.6; margin: 0 0 18px; max-width: 820px; }
  .deep-dive p { font-size: 13.5px; color: var(--text-secondary); line-height: 1.7; max-width: 820px; margin: 0 0 14px; }
  .open-q { border-left: 3px solid var(--accent); background: var(--accent-soft); border-radius: 6px; padding: 10px 14px; font-size: 12.5px; color: var(--text-primary); line-height: 1.55; max-width: 780px; }
  :root[data-theme="dark"] .open-q { color: var(--text-secondary); }
  .open-q b { color: var(--accent); }

  .steps { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 6px; }
  .step-chip { background: var(--surface-3); border: 1px solid var(--border); border-radius: 999px; padding: 4px 10px; font-size: 11.5px; color: var(--text-secondary); }

  table.risk-table { width: 100%; border-collapse: collapse; font-size: 12.5px; margin-top: 8px; }
  table.risk-table th { text-align: left; font-size: 10.5px; text-transform: uppercase; letter-spacing: .03em; color: var(--text-muted); font-weight: 700; padding: 6px 10px; border-bottom: 1px solid var(--border); }
  table.risk-table td { padding: 9px 10px; border-bottom: 1px solid var(--border); vertical-align: top; color: var(--text-primary); }
  table.risk-table tr:last-child td { border-bottom: none; }
  .rt-variable { font-weight: 700; white-space: nowrap; }
  .rt-source { color: var(--text-muted); font-size: 11px; }
  .badge { display: inline-flex; align-items: center; gap: 3px; font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 5px; line-height: 1.6; }
  .badge.good { color: var(--good); background: var(--good-bg); }
  .badge.warning { color: #a8720c; background: var(--warning-bg); }
  .badge.critical { color: var(--critical); background: var(--critical-bg); }
  .badge svg { width: 9px; height: 9px; }

  .cc-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 8px; }
  .cc-card { background: var(--surface-2); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; }
  .cc-card .cc-title { font-size: 12.5px; font-weight: 700; margin-bottom: 4px; }
  .cc-card .cc-body { font-size: 12px; color: var(--text-secondary); line-height: 1.5; }

  /* map */
  .map-caption { font-size: 13px; color: var(--text-secondary); line-height: 1.55; margin: 0 0 14px; max-width: 820px; }
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
  .marker.dimmed circle.dot { opacity: 0.25; }

  .side-panel { background: var(--surface-2); border: 1px solid var(--border); border-radius: 12px; padding: 16px 18px; min-height: 260px; }
  .side-panel h3.loc-name { font-size: 15px; margin: 0 0 2px; }
  .side-panel .loc-meta { font-size: 12px; color: var(--text-muted); margin-bottom: 10px; }
  .type-pill { display: inline-flex; align-items: center; gap: 5px; font-size: 11px; font-weight: 700; padding: 3px 9px; border-radius: 999px; background: var(--surface-3); color: var(--text-secondary); margin-bottom: 10px; }
  .type-pill .chip-dot { width: 8px; height: 8px; }
  .side-panel .note { font-size: 13px; color: var(--text-secondary); line-height: 1.55; margin-bottom: 12px; }
  .risk-callout { border-left: 3px solid var(--warning); background: var(--warning-bg); border-radius: 6px; padding: 10px 12px; font-size: 12.5px; color: var(--text-primary); line-height: 1.5; }
  :root[data-theme="dark"] .risk-callout { color: var(--text-secondary); }
  .risk-callout b { display: block; margin-bottom: 3px; font-size: 12px; }
  .placeholder { color: var(--text-muted); font-size: 13px; line-height: 1.6; }
  .legend-block { margin-top: 18px; }
  .legend-block h4 { font-size: 11px; text-transform: uppercase; letter-spacing: .03em; color: var(--text-muted); margin: 0 0 8px; }
  .legend-row { display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--text-secondary); margin-bottom: 6px; }
  .legend-swatch { width: 13px; height: 13px; border-radius: 3px; flex: none; }

  .footer-note { margin-top: 20px; font-size: 11.5px; color: var(--text-muted); line-height: 1.6; }

  /* prev/next nav */
  .step-footer-nav { display: flex; justify-content: space-between; align-items: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--border); gap: 12px; flex-wrap: wrap; }
  .nav-link { text-decoration: none; color: var(--text-secondary); font-size: 13px; font-weight: 600; padding: 10px 16px; border: 1px solid var(--border); border-radius: 10px; background: var(--surface-2); transition: border-color .15s ease; max-width: 46%; }
  .nav-link:hover { border-color: var(--accent); color: var(--accent); }
  .nav-link .nav-dir { display: block; font-size: 10px; text-transform: uppercase; letter-spacing: .04em; color: var(--text-muted); margin-bottom: 3px; }
  .nav-link.overview-link { text-align: center; max-width: none; }

  @media (max-width: 880px) {
    .content { grid-template-columns: 1fr; }
    .cc-grid { grid-template-columns: 1fr; }
  }
"""


def render_page(stage, idx):
    prev_stage = STAGES[idx - 1] if idx > 0 else None
    next_stage = STAGES[idx + 1] if idx < len(STAGES) - 1 else None

    pills = ""
    for s in STAGES:
        cur = " current" if s["id"] == stage["id"] else ""
        pills += f'<a class="step-pill{cur}" href="{s["url"]}"><span class="num-badge">{s["num"]}</span>{s["title"]}</a>\n'

    steps_chips = "".join(f'<span class="step-chip">{st}</span>' for st in stage["steps"])

    def risk_icon(level):
        if level == "good":
            return '<svg viewBox="0 0 16 16" fill="none"><path d="M3 8.5L6.5 12L13 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        if level == "warning":
            return '<svg viewBox="0 0 16 16" fill="none"><path d="M8 2L14.5 13H1.5L8 2Z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M8 6.5V9.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="8" cy="11.3" r="0.9" fill="currentColor"/></svg>'
        return '<svg viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6.5" stroke="currentColor" stroke-width="1.6"/><path d="M8 5V8.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="8" cy="10.8" r="0.9" fill="currentColor"/></svg>'

    def risk_label(level):
        return {"good": "Low", "warning": "Medium", "critical": "High"}[level]

    risk_rows = ""
    for r in stage["risks"]:
        risk_rows += f"""
          <tr>
            <td class="rt-variable">{r['variable']}</td>
            <td><span class="badge {r['level']}">{risk_icon(r['level'])}{risk_label(r['level'])}</span></td>
            <td>{r['text']}</td>
            <td class="rt-source">{r['source']}</td>
          </tr>"""

    deep_dive_html = "".join(f"<p>{p}</p>" for p in stage["deep_dive"])
    open_q_html = f'<div class="open-q"><b>Open question: </b>{stage["open_question"]}</div>' if stage.get("open_question") else ""

    cc_html = "".join(f'<div class="cc-card"><div class="cc-title">{c["title"]}</div><div class="cc-body">{c["body"]}</div></div>' for c in CROSSCUT)

    prev_html = f'<a class="nav-link" href="{prev_stage["url"]}"><span class="nav-dir">← Previous step</span>Step {prev_stage["num"]} — {prev_stage["title"]}</a>' if prev_stage else '<span></span>'
    next_html = f'<a class="nav-link" href="{next_stage["url"]}" style="text-align:right"><span class="nav-dir">Next step →</span>Step {next_stage["num"]} — {next_stage["title"]}</a>' if next_stage else '<span></span>'

    html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UltraTech Cement — Step __NUM__: __TITLE__</title>
<style>__SHARED_CSS__</style>
</head>
<body>
<div class="viz-root" id="vizRoot">
  <div class="wrap">
    <div class="top-bar">
      <div>
        <h1>Step __NUM__ — __TITLE__</h1>
        <p class="subtitle">__SUMMARY__</p>
        <div class="breadcrumb"><a href="ultratech_overview.html">← Back to Overview</a> &nbsp;·&nbsp; Process & Risk Map</div>
      </div>
      <button class="theme-toggle" id="themeToggle">Dark mode</button>
    </div>

    <div class="step-nav">
__PILLS__
    </div>

    <h2 class="section-title">What happens here</h2>
    <div class="steps">__STEPS_CHIPS__</div>

    <h2 class="section-title">In detail</h2>
    <div class="deep-dive">__DEEP_DIVE__</div>
    __OPEN_Q__

    <h2 class="section-title">Risk variables at this step</h2>
    <table class="risk-table">
      <thead><tr><th style="width:170px">Variable</th><th style="width:70px">Risk</th><th>What we found</th><th style="width:160px">Source</th></tr></thead>
      <tbody>__RISK_ROWS__
      </tbody>
    </table>
    <div class="cc-grid">__CC_HTML__</div>

    <h2 class="section-title">Where this happens</h2>
    <p class="map-caption">__MAP_CAPTION__</p>
    <div class="controls">
      <div class="control-group">
        <span class="control-label">Show:</span>
        <label class="chip-toggle"><input type="checkbox" class="type-cb" value="integrated"><span class="chip-dot" style="background:#2a78d6"></span>Integrated plants</label>
        <label class="chip-toggle"><input type="checkbox" class="type-cb" value="grinding"><span class="chip-dot" style="background:#eb6834"></span>Grinding units</label>
        <label class="chip-toggle"><input type="checkbox" class="type-cb" value="hub"><span class="chip-dot" style="background:#1baf7a"></span>Bulk / RMC hubs</label>
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
        <div class="placeholder">Click any highlighted marker to see details. Locations relevant to this step are shown by default — use the checkboxes to reveal other facility types too.</div>
        <div class="legend-block">
          <h4>Facility type</h4>
          <div class="legend-row"><span class="legend-swatch" style="background:#2a78d6"></span>Integrated plant</div>
          <div class="legend-row"><span class="legend-swatch" style="background:#eb6834"></span>Grinding unit</div>
          <div class="legend-row"><span class="legend-swatch" style="background:#1baf7a"></span>Bulk terminal / RMC hub</div>
        </div>
      </div>
    </div>
    <div class="footer-note">For the full India map with all facility types plus the International Footprint (UAE, Bahrain, Sri Lanka), see the <a href="ultratech_overview.html#map">Overview page</a>.</div>

    <div class="step-footer-nav">
      __PREV_HTML__
      <a class="nav-link overview-link" href="ultratech_overview.html">All steps</a>
      __NEXT_HTML__
    </div>
  </div>
</div>

<script>
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

const STATE_DATA = __STATE_DATA__;
const LOCATIONS = __LOCATIONS__;
const RISK_NOTES = __RISK_NOTES__;
const TYPE_META = __TYPE_META__;
const BOUNDS = __BOUNDS__;
const FOCUS_TYPES = __FOCUS_TYPES__;

function project(lon, lat) {
  const x = (lon - BOUNDS.minx) * BOUNDS.cos_lat;
  const y = (BOUNDS.maxy - lat);
  return [x, y];
}

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
  g.setAttribute("class", "marker" + (FOCUS_TYPES.includes(loc.type) ? "" : " dimmed"));
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
  if (!FOCUS_TYPES.includes(loc.type)) g.style.display = "none";
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
    <h3 class="loc-name">${loc.name}</h3>
    <div class="loc-meta">${loc.city} · ${loc.state}</div>
    <div class="type-pill"><span class="chip-dot" style="background:${meta.color}"></span>${meta.label}</div>
    <div class="note">${loc.note}</div>
    ${riskHtml}
  `;
}

// preset checkboxes to focus types
document.querySelectorAll(".type-cb").forEach(cb => {
  cb.checked = FOCUS_TYPES.includes(cb.value);
});
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
</script>
</body>
</html>
"""
    html = html.replace("__NUM__", stage["num"])
    html = html.replace("__TITLE__", stage["title"])
    html = html.replace("__SUMMARY__", stage["summary"])
    html = html.replace("__PILLS__", pills)
    html = html.replace("__STEPS_CHIPS__", steps_chips)
    html = html.replace("__DEEP_DIVE__", deep_dive_html)
    html = html.replace("__OPEN_Q__", open_q_html)
    html = html.replace("__RISK_ROWS__", risk_rows)
    html = html.replace("__CC_HTML__", cc_html)
    html = html.replace("__MAP_CAPTION__", stage["map_caption"])
    html = html.replace("__PREV_HTML__", prev_html)
    html = html.replace("__NEXT_HTML__", next_html)
    html = html.replace("__VIEWBOX__", states_data["viewBox"])
    html = html.replace("__SHARED_CSS__", SHARED_CSS)
    html = html.replace("__STATE_DATA__", json.dumps(states_data))
    html = html.replace("__LOCATIONS__", json.dumps(LOCATIONS))
    html = html.replace("__RISK_NOTES__", json.dumps(RISK_NOTES))
    html = html.replace("__TYPE_META__", json.dumps(TYPE_META))
    html = html.replace("__BOUNDS__", json.dumps(bounds))
    html = html.replace("__FOCUS_TYPES__", json.dumps(stage["map_types"]))
    return html


for idx, stage in enumerate(STAGES):
    page = render_page(stage, idx)
    path = f"/home/claude/equity_research/{stage['url']}"
    open(path, "w").write(page)
    print("wrote", path, len(page))
