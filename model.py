import random

# 1. Core Project Infrastructure Constraints
CAPEX = 200_000_000
OPEX_BASE = 4_000_000
ASSET_LIFE = 25
DISCOUNT_RATE = 0.07          # Tier-1 UK infrastructure WACC proxy
NUM_SIMULATIONS = 500
ANNUAL_GENERATION_MWH = 454222
TAX_RATE = 0.25
ANNUAL_DEPRECIATION = CAPEX / ASSET_LIFE  # Capital allowance tax proxy
PRICE_FLOOR_CFD = 40.00       # UK Contract for Difference (CfD) floor price proxy

profitable_count = 0
all_npvs = []

# 2. Stochastic Risk Simulation Engine
for i in range(NUM_SIMULATIONS):
    # Year 0: Pure Capital Outflow
    cash_flows = [-CAPEX]
    
    for year in range(1, ASSET_LIFE + 1):
        # Market Uncertainty Vectors
        raw_price = random.gauss(65, 12)
        opex_scaler = random.uniform(0.95, 1.05)

        # Apply Price Floor Protection
        elec_price = max(raw_price, PRICE_FLOOR_CFD)

        # Financial Operations Engine
        revenue = ANNUAL_GENERATION_MWH * elec_price
        costs = OPEX_BASE * opex_scaler
        ebitda = revenue - costs
        
        # Correct Corporate Tax Shield Treatment
        taxable_income = max(0, ebitda - ANNUAL_DEPRECIATION)
        tax_paid = taxable_income * TAX_RATE
        net_cash_flow = ebitda - tax_paid
        
        cash_flows.append(net_cash_flow)

    # Time-value of money discounting loop
    npv = sum(cf / (1 + DISCOUNT_RATE)**t for t, cf in enumerate(cash_flows))
    all_npvs.append(npv)
    if npv > 0:
        profitable_count += 1

# 3. Print Institutional Performance Metrics
mean_npv = sum(all_npvs) / len(all_npvs)
prob_profitable = (profitable_count / NUM_SIMULATIONS) * 100

print("=========================================")
print("📊 STOCHASTIC SIMULATION RESULTS")
print("=========================================")
print(f"Expected Average Return (NPV): £{mean_npv:,.2f}")
print(f"Probability of Breaking Even: {prob_profitable:.1f}%")
print("=========================================")

# 4. Stabilized Static Text Graph (Fixed £10M Bins from -£20M to £80M)
print("\n📈 VISUAL FINANCIAL RISK DISTRIBUTION GRAPH:")
fixed_bins = [0] * 10
bin_width = 10_000_000
lower_bound = -20_000_000

for npv in all_npvs:
    bin_idx = int((npv - lower_bound) // bin_width)
    if 0 <= bin_idx < 10:
        fixed_bins[bin_idx] += 1

bin_labels = [
    "-£20M to -£10M", "-£10M to £0M  ", " £0M to £10M  ", " £10M to £20M ", 
    " £20M to £30M ", " £30M to £40M ", " £40M to £50M ", " £50M to £60M ", 
    " £60M to £70M ", " £70M+         "
]

for label, count in zip(bin_labels, fixed_bins):
    bar = "█" * (count // 4)  # Scales display density cleanly
    print(f"{label}: {bar}")
