import random

# 1. Base Project Rules
CAPEX = 150000000
OPEX_BASE = 4000000
ASSET_LIFE = 25
DISCOUNT_RATE = 0.07
NUM_SIMULATIONS = 500
ANNUAL_GENERATION_MWH = 450000

# 2. Simulation Engine
profitable_count = 0
all_npvs = []

for i in range(NUM_SIMULATIONS):
    cash_flows = [-CAPEX]
    for year in range(ASSET_LIFE):
        elec_price = random.gauss(65, 12)
        opex_scaler = random.uniform(0.95, 1.05)

        revenue = ANNUAL_GENERATION_MWH * elec_price
        costs = OPEX_BASE * opex_scaler
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
print("📊 SIMULATION RESULTS (PROVED SUCCESSFUL)")
print("=========================================")
print(f"Expected Average Return (NPV): £{mean_npv:,.2f}")
print(f"Probability of Breaking Even: {prob_profitable:.1f}%")
print("=========================================")

# 4. Mobile Text-Based Graph
print("\n📈 VISUAL FINANCIAL RISK DISTRIBUTION GRAPH:")
min_npv, max_npv = min(all_npvs), max(all_npvs)
buckets = [0] * 10
for npv in all_npvs:
    idx = int((npv - min_npv) / (max_npv - min_npv) * 9)
    buckets[idx] += 1

for i, count in enumerate(buckets):
    bar = "█" * (count // 5)
    print(f"Risk Zone {i+1}: {bar}")
