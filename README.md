# UK-Power-Market-Investment-Model
### Built using Python and Excel, this is a quantitative asset valuation model and Monte Carlo risk engine.   This project simulates 25 years of UK electrical price volatility and supply chain inflation. By running simulation cycles, it translates market fluctuations into interpretable financial metrics.





This project is an Asset-Level Stochastic Financial Risk Valuation Engine.
This tool is designed to simulate and stress-test the financial forecasting of a £150M utility infrastructure project, such as a wind farm of a nuclear power plant, under conditions of extreme macroeconomic volatility.   

The tool tests the break-even probability of the asset over 25 years, isolating how market shocks, such as wholesale power price collapse, impact the project's Net Project Value (NPV). 
Traditional financial models assume fixed, flat electricity prices every year, ignoring realistic market crashes. This project however, creates 500 independent, paralle-universe type lifecycles. 

To execute this, I engineered a Monte Carlo simulation loop in Python, ensuring a highly auditable codebase. I used a Guassian distribution to model wholesale electrical prices, I anchored the mean at the UK's historical £65/MWh baseline, with a standard deviation of £12. This mathematically guarantees a 95% market swing capture between £41-89/MWh.
To simulate supply chain friction, I subjected the assigned £4M baseline cost to a Uniform Continuous Distribution of +/-5% annually. 
The script flows into a Discounted Cash Flow (DCF), to which a 25% corporate tax proxy to isolate net cash is applied, which then discounts those flows back to Year 0 using a discount rate of 7%, a standard Weighted Average Cost of Capital (WACC) for tier-1 UK infrastructure.



## 🖥️ Live Simulation Execution Output

Below is the verified structural compiler output demonstrating the risk-engine calculations:

```text
=========================================
📊 SIMULATION RESULTS (PROVED SUCCESSFUL)
=========================================
Expected Average Return (NPV): £70,122,190.64
Probability of Breaking Even: 100.0%
=========================================

📈 VISUAL FINANCIAL RISK DISTRIBUTION GRAPH:

Risk Zone 1  | 
Risk Zone 2  | ██
Risk Zone 3  | ████████
Risk Zone 4  | █████████████████
Risk Zone 5  | █████████████████████████  <-- Expected Mean (£70.1M)
Risk Zone 6  | ███████████████████████
Risk Zone 7  | ██████████████
Risk Zone 8  | ██████
Risk Zone 9  | █
Risk Zone 10 | 
             +---------------------------------------------------
  (X-Axis)   | £30M   £40M   £50M   £60M   £70M   £80M   £90M   £100M+
  Units:     | Net Present Value (NPV) in Millions of Pounds (£M)
```

