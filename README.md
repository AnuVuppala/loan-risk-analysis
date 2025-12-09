# Loan Default Risk Analysis

This project analyzes borrower data to identify risk patterns and recommend collection/lending strategies.

Files:
- loan_data.csv : synthetic dataset (500 rows)
- data_generator.py : script to generate the dataset (optional)
- loan_analysis.py : Python analysis that creates visuals and top-10 risk list
- visuals/ : generated charts (emi_vs_default.png, credit_score_defaults.png)
- top10_risk.csv : top 10 high-risk borrowers
- insights.txt : summary of findings and recommendations

Tools:
- Python (pandas, matplotlib)
- Excel (optional for pivots)
- Power BI (mockup dashboard in powerbi-sample repo)

How to run:
1. python data_generator.py  # to create loan_data.csv
2. python loan_analysis.py   # to run analysis and create visuals
