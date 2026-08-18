import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

FONT = "Arial"

wb = openpyxl.Workbook()

# ---------- Styles ----------
title_font = Font(name=FONT, size=16, bold=True, color="FFFFFF")
title_fill = PatternFill("solid", fgColor="1F3864")
header_font = Font(name=FONT, size=11, bold=True, color="FFFFFF")
header_fill = PatternFill("solid", fgColor="2E5395")
cat_font = Font(name=FONT, size=11, bold=True, color="FFFFFF")
cat_fill = PatternFill("solid", fgColor="8EA9DB")
body_font = Font(name=FONT, size=10)
body_font_bold = Font(name=FONT, size=10, bold=True)
wrap = Alignment(wrap_text=True, vertical="top", horizontal="left")
wrap_center = Alignment(wrap_text=True, vertical="center", horizontal="center")
thin = Side(style="thin", color="D9D9D9")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

RISK_FILL = {
    "High": PatternFill("solid", fgColor="F8696B"),
    "Medium": PatternFill("solid", fgColor="FFEB84"),
    "Low": PatternFill("solid", fgColor="63BE7B"),
    "TBD": PatternFill("solid", fgColor="D9D9D9"),
}

def style_header_row(ws, row, ncols, fill=header_fill, font=header_font):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = font
        cell.fill = fill
        cell.alignment = wrap_center
        cell.border = border

def set_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

# =====================================================================
# SHEET 1: How to Use
# =====================================================================
ws = wb.active
ws.title = "How to Use"
set_widths(ws, [110])
ws.row_dimensions[1].height = 30
ws["A1"] = "Business Variable Framework — Equity Research Base Tool"
ws["A1"].font = title_font
ws["A1"].fill = title_fill
ws["A1"].alignment = Alignment(vertical="center", horizontal="left", indent=1)

lines = [
    "",
    "PURPOSE",
    "This is the reusable base of a bigger equity-research tool. Before valuing any company, you first need to",
    "understand its business - what makes it work, and what could break it. This workbook is a checklist of the",
    "'variables' that matter for ANY company, applied here to UltraTech Cement as a worked example.",
    "",
    "HOW THE SHEETS FIT TOGETHER",
    "1. 'Variable Framework' - the master checklist. ~30 questions grouped into 7 categories (raw materials,",
    "   geography, regulation, customers, competition, cost structure, ownership/financials). This list is",
    "   sector-agnostic - reuse it for every company you research.",
    "2. 'UltraTech Cement (Example)' - the same checklist, filled in with real findings for UltraTech, plus a",
    "   Risk/Impact rating for each variable and a source. This is the template for how every future company",
    "   should be filled in.",
    "3. 'Company Comparison' - the same variables laid out with one column per company, so once you research a",
    "   second and third company (e.g. Ambuja Cement, Shree Cement) you can see them side by side.",
    "",
    "HOW TO ADD A NEW COMPANY",
    "- Duplicate the 'UltraTech Cement (Example)' sheet, rename it to the new company, and fill in the Finding /",
    "  Risk / Source columns.",
    "- Add a new column in 'Company Comparison' with that company's short answers.",
    "",
    "RISK / IMPACT RATING - what it means",
    "- High: this variable could meaningfully hurt the business if it goes wrong (e.g. losing captive limestone",
    "  mines, a coal price spike, a regional demand crash).",
    "- Medium: matters, but the company has some buffer or it's a slower-moving risk.",
    "- Low: unlikely to move the needle much, or the company is well insulated from it.",
    "- TBD: not yet researched - a gap to fill in next.",
    "",
    "NEXT STEPS",
    "- Research a second cement company (Ambuja/ACC or Shree Cement) using this same checklist.",
    "- Once 2-3 companies in a sector are done, move to Step 2 of the plan: industry-level analysis.",
]
for i, line in enumerate(lines, start=2):
    cell = ws.cell(row=i, column=1, value=line)
    cell.font = body_font_bold if line.isupper() else body_font
    cell.alignment = Alignment(wrap_text=True, vertical="top")

# =====================================================================
# Shared data: the variable framework (category, variable, guiding question, why it matters)
# =====================================================================
FRAMEWORK = [
    ("Raw Material & Input Sourcing", [
        ("Key inputs", "What raw materials/inputs does the company need to make its product?", "Defines the company's core cost base and supply chain."),
        ("Source location", "Where are those inputs sourced from (which region/state/country)?", "A single-region source is a concentration risk - local disruption hits the whole company."),
        ("Captive vs. open market", "Does the company own the source (captive mine/well/farm) or buy on the open market?", "Captive sourcing insulates from price spikes; open-market buyers are exposed to commodity cycles."),
        ("Supplier concentration", "How many suppliers are there, and how much power do they have?", "Few powerful suppliers can squeeze margins or disrupt supply."),
        ("Input price volatility", "Is the input price volatile / linked to a global commodity?", "Volatile inputs create earnings swings the company may or may not be able to pass on."),
        ("Substitutability", "If supply is disrupted, are there substitutes or alternate sources?", "No substitute = higher risk from any single-source disruption."),
    ]),
    ("Geography & Logistics", [
        ("Facility locations", "Where are the company's plants/offices/stores located?", "Determines proximity to both inputs and customers."),
        ("Distance to market", "How far are facilities from key demand centers (the 'freight radius')?", "For heavy/bulky products, transport cost can exceed the profit margin beyond a certain distance."),
        ("Logistics cost share", "What % of total cost is freight/transportation/logistics?", "High logistics share makes location a competitive advantage or disadvantage."),
        ("Regional concentration risk", "Is revenue/production concentrated in one state/region?", "A local disruption (weather, unrest, policy change) can hit disproportionately."),
    ]),
    ("Regulatory & Political", [
        ("Licenses & permits", "What licenses/permits are required to operate (mining, environmental, etc.)?", "Licenses can be delayed, denied, or revoked - a direct operating risk."),
        ("Regulating authority", "Which government bodies regulate the business - central, state, or both?", "State-level rules can vary a lot within one country and change with local politics."),
        ("Regulatory disputes", "Any pending or historical regulatory/legal disputes?", "Ongoing disputes signal risk of fines, shutdowns, or reputational damage."),
        ("Trade policy exposure", "Any import/export duties or restrictions on inputs or outputs?", "Tariff changes can swing costs or competitiveness overnight."),
        ("Environmental/ESG exposure", "How exposed is the business to environmental regulation (emissions, waste, land use)?", "Tightening environmental rules can raise costs or restrict operations, especially in heavy industry."),
    ]),
    ("Customers & Demand", [
        ("Customer type", "Who buys the product - other businesses (B2B), consumers (B2C), or government?", "Different buyer types have very different bargaining power and payment behavior."),
        ("Customer concentration", "Are sales concentrated among a few large customers, or spread across many small ones?", "Few large customers = they can dictate price/terms; many small customers = pricing power stays with the seller."),
        ("Demand driver", "What macro factor drives demand (GDP growth, consumer spending, construction activity, etc.)?", "Tells you what to watch to predict the company's demand before it shows up in results."),
        ("Cyclicality/seasonality", "Is demand cyclical (tied to economic cycles) or seasonal (tied to time of year)?", "Affects how to read quarter-to-quarter swings and time an investment."),
    ]),
    ("Competition & Market Structure", [
        ("Market concentration", "How many real competitors are there, and how much market share do the top few hold?", "Fragmented markets = price competition; concentrated markets = more pricing discipline."),
        ("Competitive arena", "Is competition local/regional, national, or global?", "Determines who the company is really fighting for customers against."),
        ("Barriers to entry", "What stops a new competitor from entering (capital needs, regulation, brand, patents)?", "High barriers protect margins over the long run; low barriers invite new competition."),
        ("Pricing power", "Can the company raise prices without losing significant volume?", "Pricing power is one of the strongest signs of a durable, high-quality business."),
    ]),
    ("Cost Structure & Capital Intensity", [
        ("Fixed vs. variable costs", "What's the mix of fixed costs (rent, plant) vs. variable costs (materials, per-unit labor)?", "High fixed costs mean profits swing a lot with volume (operating leverage)."),
        ("Capital intensity", "How much capital does it take to build new capacity or enter the business?", "Capital-heavy businesses are slower to expand and harder for new entrants to copy."),
        ("Returns trend", "Are returns on new investment/capacity rising or falling over time?", "Falling returns on new capacity is an early warning sign for the whole industry's profitability."),
    ]),
    ("Ownership & Financials", [
        ("Ownership structure", "Who owns/controls the company (founder/promoter group, government, widely-held public)?", "Ownership shapes incentives, capital allocation discipline, and related-party risk."),
        ("Financial leverage", "How much debt does the company carry relative to its earnings?", "High leverage amplifies both upside and downside, and raises bankruptcy risk in downturns."),
        ("Currency exposure", "Does the company import inputs, export output, or operate abroad in foreign currency?", "Currency swings can move costs or revenue even when the underlying business is unchanged."),
    ]),
]

# =====================================================================
# SHEET 2: Variable Framework (master checklist, sector-agnostic)
# =====================================================================
ws2 = wb.create_sheet("Variable Framework")
headers = ["#", "Category", "Variable", "Guiding Question", "Why It Matters"]
set_widths(ws2, [5, 24, 22, 46, 46])
for c, h in enumerate(headers, start=1):
    ws2.cell(row=1, column=c, value=h)
style_header_row(ws2, 1, len(headers))
ws2.row_dimensions[1].height = 20
ws2.freeze_panes = "A2"

row = 2
idx = 1
for category, items in FRAMEWORK:
    for var, question, why in items:
        ws2.cell(row=row, column=1, value=idx).font = body_font
        ws2.cell(row=row, column=2, value=category).font = body_font
        ws2.cell(row=row, column=3, value=var).font = body_font_bold
        ws2.cell(row=row, column=4, value=question).font = body_font
        ws2.cell(row=row, column=5, value=why).font = body_font
        for c in range(1, 6):
            ws2.cell(row=row, column=c).alignment = wrap
            ws2.cell(row=row, column=c).border = border
        row += 1
        idx += 1

# =====================================================================
# UltraTech findings: variable -> (finding, risk, source)
# =====================================================================
SRC_STRATEGY = "The Strategy Story - UltraTech Business Model 2026"
SRC_SAFAL = "Safal Niveshak - Cement Industry Analysis"
SRC_VARSITY = "Zerodha Varsity - Cement Industry Analysis"
SRC_USER = "Not yet researched"

ULTRATECH = {
    "Key inputs": ("Limestone, clay, silica, gypsum (raw materials) + coal/petcoke (kiln fuel) + power.", "Medium", SRC_SAFAL),
    "Source location": ("Raw materials sourced near plant sites across India (e.g. Chhattisgarh limestone); coal from domestic linkages plus some imports.", "Medium", SRC_VARSITY),
    "Captive vs. open market": ("UltraTech owns captive limestone quarries (plants built near them) and holds captive coal mine linkages - a real cost advantage vs. smaller players who buy coal/petcoke on the open market.", "Low", SRC_VARSITY),
    "Supplier concentration": ("Largely self-supplied for limestone via captive mines; coal linkage plus market purchases reduce single-supplier dependence, though global coal/petcoke prices still matter.", "Medium", SRC_VARSITY),
    "Input price volatility": ("Coal/petcoke prices are volatile and are the single biggest swing factor in cement costs (~160kg coal per tonne of cement).", "High", SRC_SAFAL),
    "Substitutability": ("Limited fuel substitutes at scale, though UltraTech is investing in waste heat recovery and renewables to cover 25-30% of energy needs, reducing fossil fuel dependence over time.", "Medium", SRC_VARSITY),
    "Facility locations": ("200+ MTPA grey cement capacity across India, plus operations in UAE, Bahrain, Sri Lanka; 465 RMC plants across 167 cities.", "Low", SRC_STRATEGY),
    "Distance to market": ("Cement plants typically serve customers within a 150-300 km radius due to transport economics; UltraTech's scale gives it wide geographic coverage (90%+ of India's talukas).", "Medium", SRC_SAFAL),
    "Logistics cost share": ("Freight/transportation is roughly 20-25% of sales industry-wide - often bigger than net profit margin - making plant location and distribution network critical.", "High", SRC_SAFAL),
    "Regional concentration risk": ("Diversified nationally with plants across regions rather than concentrated in one state, which reduces (but doesn't eliminate) local disruption risk.", "Low", SRC_STRATEGY),
    "Licenses & permits": ("Requires mining leases (limestone), environmental clearances, and coal linkage allocations; large scale means constant renewal/compliance activity.", "Medium", SRC_VARSITY),
    "Regulating authority": ("Both central (environment, coal allocation) and state (mining leases, land) government bodies regulate operations - multiplies the points of regulatory risk.", "Medium", SRC_USER),
    "Regulatory disputes": ("Not yet researched - check for any pending mining/environmental litigation or local community disputes (e.g. reported concerns around Chhattisgarh mining operations).", "TBD", SRC_USER),
    "Trade policy exposure": ("Some coal is imported, so import duties/global coal prices matter; core cement business is domestic-demand driven with limited export exposure.", "Medium", SRC_USER),
    "Environmental/ESG exposure": ("Cement manufacturing is carbon- and energy-intensive; stricter emissions norms are a probable future cost driver. UltraTech is investing in renewables/waste heat recovery partly to get ahead of this.", "High", SRC_VARSITY),
    "Customer type": ("Mix of B2B (contractors, builders, infrastructure projects) and B2C (individual home-builders via dealer network), plus a growing 'Building Solutions' retail channel.", "Low", SRC_STRATEGY),
    "Customer concentration": ("Very fragmented - 1.5+ lakh channel partners and ~30,000 delivery destinations - so no single customer has meaningful bargaining power.", "Low", SRC_STRATEGY),
    "Demand driver": ("Housing, infrastructure, and industrial construction activity; demand tracks GDP growth at roughly 1.2x.", "Medium", SRC_SAFAL),
    "Cyclicality/seasonality": ("Cyclical with the broader economy/construction activity, plus a seasonal dip during the monsoon.", "Medium", SRC_SAFAL),
    "Market concentration": ("Consolidated: top 3-4 players (UltraTech, Ambuja/ACC, Shree Cement, Dalmia Bharat) hold roughly a third of industry capacity; UltraTech itself is the largest.", "Low", SRC_SAFAL),
    "Competitive arena": ("Fundamentally regional/local due to freight economics, even though UltraTech competes nationally in aggregate.", "Medium", SRC_SAFAL),
    "Barriers to entry": ("High - cement plants are extremely capital-intensive and require mining rights and environmental clearances, which naturally limits new entrants.", "Low", SRC_SAFAL),
    "Pricing power": ("Limited industry-wide - transparent local pricing tends to trigger price wars when capacity utilization is low; competition instead focuses on cost efficiency, distribution reach, and brand/product mix.", "Medium", SRC_SAFAL),
    "Fixed vs. variable costs": ("Heavy fixed-cost base (plants, mining leases) combined with variable fuel/power costs - meaning capacity utilization strongly drives per-unit profitability.", "Medium", SRC_USER),
    "Capital intensity": ("Very high - new capacity costs roughly Rs 7,200/tonne (2013 figure, higher today); UltraTech is investing ~Rs 16,000 crore to expand to 242.5 MTPA by FY2027-28.", "Medium", SRC_STRATEGY),
    "Returns trend": ("Industry-wide, returns on new cement capacity have fallen over time (IRR ~17% in 2008 to ~9% in 2013) - a red flag to monitor for future capacity additions.", "High", SRC_SAFAL),
    "Ownership structure": ("Part of the Aditya Birla Group - a large, established Indian promoter conglomerate, not government-owned or widely dispersed.", "Low", SRC_STRATEGY),
    "Financial leverage": ("Not yet researched - need to pull debt/EBITDA or debt/equity from the balance sheet.", "TBD", SRC_USER),
    "Currency exposure": ("Mostly domestic (India) revenue; some FX exposure via international operations (UAE, Bahrain, Sri Lanka) and imported coal.", "Low", SRC_USER),
}

# =====================================================================
# SHEET 3: UltraTech Cement (Example) - framework filled in
# =====================================================================
ws3 = wb.create_sheet("UltraTech Cement (Example)")
headers3 = ["#", "Category", "Variable", "Finding", "Risk / Impact", "Source"]
set_widths(ws3, [5, 22, 20, 58, 14, 30])
for c, h in enumerate(headers3, start=1):
    ws3.cell(row=1, column=c, value=h)
style_header_row(ws3, 1, len(headers3))
ws3.row_dimensions[1].height = 20
ws3.freeze_panes = "A2"

row = 2
idx = 1
for category, items in FRAMEWORK:
    for var, question, why in items:
        finding, risk, source = ULTRATECH.get(var, ("Not yet researched", "TBD", SRC_USER))
        ws3.cell(row=row, column=1, value=idx).font = body_font
        ws3.cell(row=row, column=2, value=category).font = body_font
        ws3.cell(row=row, column=3, value=var).font = body_font_bold
        ws3.cell(row=row, column=4, value=finding).font = body_font
        risk_cell = ws3.cell(row=row, column=5, value=risk)
        risk_cell.font = body_font_bold
        risk_cell.fill = RISK_FILL.get(risk, RISK_FILL["TBD"])
        risk_cell.alignment = wrap_center
        ws3.cell(row=row, column=6, value=source).font = body_font
        for c in range(1, 7):
            ws3.cell(row=row, column=c).border = border
            if c != 5:
                ws3.cell(row=row, column=c).alignment = wrap
        row += 1
        idx += 1

# Risk summary using COUNTIF formulas
last_row = row - 1
summary_row = row + 1
ws3.cell(row=summary_row, column=2, value="Risk Summary:").font = body_font_bold
ws3.cell(row=summary_row, column=3, value="High").font = body_font
ws3.cell(row=summary_row, column=4, value=f'=COUNTIF(E2:E{last_row},"High")').font = body_font
ws3.cell(row=summary_row + 1, column=3, value="Medium").font = body_font
ws3.cell(row=summary_row + 1, column=4, value=f'=COUNTIF(E2:E{last_row},"Medium")').font = body_font
ws3.cell(row=summary_row + 2, column=3, value="Low").font = body_font
ws3.cell(row=summary_row + 2, column=4, value=f'=COUNTIF(E2:E{last_row},"Low")').font = body_font
ws3.cell(row=summary_row + 3, column=3, value="TBD (research gaps)").font = body_font
ws3.cell(row=summary_row + 3, column=4, value=f'=COUNTIF(E2:E{last_row},"TBD")').font = body_font

# =====================================================================
# SHEET 4: Company Comparison (variables as rows, companies as columns)
# =====================================================================
ws4 = wb.create_sheet("Company Comparison")
headers4 = ["Category", "Variable", "UltraTech Cement", "Ambuja Cement / ACC", "Shree Cement"]
set_widths(ws4, [22, 20, 44, 34, 34])
for c, h in enumerate(headers4, start=1):
    ws4.cell(row=1, column=c, value=h)
style_header_row(ws4, 1, len(headers4))
ws4.row_dimensions[1].height = 20
ws4.freeze_panes = "A2"

# example legend row style note
row = 2
for category, items in FRAMEWORK:
    for var, question, why in items:
        finding = ULTRATECH.get(var, ("Not yet researched", "TBD", SRC_USER))[0]
        ws4.cell(row=row, column=1, value=category).font = body_font
        ws4.cell(row=row, column=2, value=var).font = body_font_bold
        ws4.cell(row=row, column=3, value=finding).font = body_font
        ws4.cell(row=row, column=4, value="").font = body_font
        ws4.cell(row=row, column=5, value="").font = body_font
        for c in range(1, 6):
            ws4.cell(row=row, column=c).alignment = wrap
            ws4.cell(row=row, column=c).border = border
        row += 1

wb.save("/home/claude/equity_research/Business_Variable_Framework.xlsx")
print("all sheets done, total rows:", row - 1)
