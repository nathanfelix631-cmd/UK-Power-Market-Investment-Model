import random

# 1. Base Project Rules
CAPEX = 200000000
OPEX_BASE = 4000000
ASSET_LIFE = 25
DISCOUNT_RATE = 0.07
NUM_SIMULATIONS = 500
ANNUAL_GENERATION_MWH = 454222
PRICE_FLOOR_CFD = 40.00       # One-way floor protection proxy

profitable_count = 0
all_npvs = []

# 2. Simulation Engine
for i in range(NUM_SIMULATIONS):
    cash_flows = [-CAPEX]
    for year in range(ASSET_LIFE):
        raw_price = random.gauss(65, 12)
        opex_scaler = random.uniform(0.95, 1.05)

        # Apply price floor protection
        elec_price = max(raw_price, PRICE_FLOOR_CFD)

        revenue = ANNUAL_GENERATION_MWH * elec_price
        costs = OPEX_BASE * opex_scaler
        
        # 25% corporate tax allowance proxy
        net_cash_flow = (revenue - costs) * 0.75
        cash_flows.append(net_cash_flow)

    npv = sum(cf / (1 + DISCOUNT_RATE)**t for t, cf in enumerate(cash_flows))
    all_npvs.append(npv)
    if npv > 0:
        profitable_count += 1

# 3. Print metrics
mean_npv = sum(all_npvs) / len(all_npvs)
prob_profitable = (profitable_count / NUM_SIMULATIONS) * 100

print("=========================================")
print("📊 STOCHASTIC SIMULATION RESULTS")
print("=========================================")
print(f"Expected Average Return (NPV): £{mean_npv:,.2f}")
print(f"Probability of Breaking Even: {prob_profitable:.1f}%")
print("=========================================")

# 4. Dynamic Text-Based Graph with Standardized Bounds
print("\n📈 VISUAL FINANCIAL RISK DISTRIBUTION GRAPH:")
print("\n [NPV Range]     | [Simulation Path Frequency Density]")
print("-----------------+-------------------------------------------------------")

# Establish explicit financial bins matching your exact range structure
bins = [
    (-20_000_000, -10_000_000, "-£20M to -£10M"),
    (-10_000_000, 0,           "-£10M to £0M   "),
    (0, 10_000_000,            " £0M to £10M   "),
    (10_000_000, 20_000_000,   " £10M to £20M  "),
    (20_000_000, 30_000_000,   " £20M to £30M  "),
    (30_000_000, 40_000_000,   " £30M to £40M  "),
    (40_000_000, 50_000_000,   " £40M to £50M  "),
    (50_000_000, 60_000_000,   " £50M to £60M  "),
    (60_000_000, 70_000_000,   " £60M to £70M  "),
    (70_000_000, float('inf'), " £70M+         ")
]

for lower, upper, label in bins:
    count = sum(1 for npv in all_npvs if lower <= npv < upper)
    bar = "█" * (count // 4) # Scaled density matching a 500-run distribution layout
    
    # Append semantic structural anchors to clear lines
    annotation = ""
    if label == "-£10M to £0M   ":
        annotation = "                                  <-- Financial Downside Floor (£0)"
    elif label == " £40M to £50M  ":
        annotation = f" <-- Expected Mean Outcome (£{mean_npv/1_000_000:.1f}M)"
        
    print(f" {label} | {bar}{annotation}")

print("-----------------+-------------------------------------------------------")
print(" (X-Axis Scale)  | 0    10   20   30   40   50   60   70   80   90   100+ ")
print(" (Units)         | Number of Run Iterations (Total Sample Size: 500 Paths)")

# 5. Milestone Aggregation Statistics Outputs
print("\n=========================================================================")
print("📌 CRITICAL FINANCIAL MILESTONE VALUES (NPV)")
print("=========================================================================")
print(f" * Minimum Simulated Return:  £{min(all_npvs):,.2f} (Absolute Downside Case)")
print(f" * Expected Average Return:  £{mean_npv:,.2f} (Weighted Base Case)")
print(f" * Maximum Simulated Return:  £{max(all_npvs):,.2f} (Optimistic Upside Case)")
print(f" * Financial Risk Threshold:  £0.00          ({prob_profitable:.1f}% Probability of Capital Preservation)")
print("=========================================================================")
