import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Base Assumptions for a Renewable / Infrastructure Asset (e.g., Wind/Solar)
CAPEX = 150_000_000       # Initial construction cost (£)
OPEX_BASE = 4_000_000     # Annual fixed operations cost (£)
ASSET_LIFE = 25           # Lifespan in years
DISCOUNT_RATE = 0.07       # Weighted Average Cost of Capital (WACC)
NUM_SIMULATIONS = 2000    # Number of Monte Carlo iterations

# Target Generation Parameters
ANNUAL_GENERATION_MWH = 450_000  # MWh generated per year

print(f"Initializing simulation for £{CAPEX:,} asset over {ASSET_LIFE} years...")

# 2. Monte Carlo Simulation Engine
np.random.seed(42) # For reproducibility
all_npvs = []

for i in range(NUM_SIMULATIONS):
    # Model uncertainty: Market prices fluctuate unpredictably each year
    # Electricity price mean = £65/MWh with standard deviation of £12
    elec_prices = np.random.normal(loc=65, scale=12, size=ASSET_LIFE)
    
    # OPEX fluctuates with inflation/supply chain variables (+/- 5%)
    opex_scalers = np.random.uniform(low=0.95, high=1.05, size=ASSET_LIFE)
    
    cash_flows = [-CAPEX] # Year 0 investment Outflow
    
    for year in range(ASSET_LIFE):
        revenue = ANNUAL_GENERATION_MWH * elec_prices[year]
        costs = OPEX_BASE * opex_scalers[year]
        net_profit = revenue - costs
        
        # Simple tax/corporate cash flow proxy (approx 75% retained)
        net_cash_flow = net_profit * 0.75 
        cash_flows.append(net_cash_flow)
        
    # Calculate Net Present Value (NPV)
    npv = np.npv(DISCOUNT_RATE, cash_flows) if hasattr(np, 'npv') else sum(cf / (1 + DISCOUNT_RATE)**t for t, cf in enumerate(cash_flows))
    all_npvs.append(npv)

# 3. Analyze Results
df_results = pd.DataFrame(all_npvs, columns=['NPV'])
prob_profitable = (df_results['NPV'] > 0).mean() * 100

print(f"\n--- Simulation Results ---")
print(f"Expected Mean NPV: £{df_results['NPV'].mean():,.2f}")
print(f"5th Percentile (Downside Risk): £{df_results['NPV'].quantile(0.05):,.2f}")
print(f"95th Percentile (Upside Potential): £{df_results['NPV'].quantile(0.95):,.2f}")
print(f"Probability of Positive Return (NPV > 0): {prob_profitable:.1f}%")
