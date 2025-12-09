# loan_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("loan_data.csv")

# Quick cleaning
df = df.drop_duplicates()
df["EMI_Ratio"] = df["EMI"] / df["Income"]

# Summary stats
print("Overall default rate:", df["Current_Default"].mean())
print("\nCredit Score distribution:\n", df["Credit_Score"].describe())

# Default rate by credit score bins
bins = [300,500,650,750,900]
labels = ["300-500","500-650","650-750","750-900"]
df["Credit_Range"] = pd.cut(df["Credit_Score"], bins=bins, labels=labels, include_lowest=True)
score_default = df.groupby("Credit_Range")["Current_Default"].mean()
print("\nDefault rate by credit score range:\n", score_default)

# Save chart: credit score default rates
score_default.plot(kind="bar", title="Default Rate by Credit Score Range")
plt.ylabel("Default Rate")
plt.savefig("visuals/credit_score_defaults.png")
plt.clf()

# EMI Ratio vs Default scatter
plt.scatter(df["EMI_Ratio"], df["Current_Default"], alpha=0.3)
plt.xlabel("EMI-to-Income Ratio")
plt.ylabel("Default (0/1)")
plt.title("EMI Ratio vs Default")
plt.savefig("visuals/emi_vs_default.png")
plt.clf()

# Top risk borrowers
df["Risk_Score"] = df["EMI_Ratio"]*0.5 + (1 - (df["Credit_Score"]-300)/600)*0.4 + (df["Past_Defaults"]>0)*0.1
top_risk = df.sort_values("Risk_Score", ascending=False).head(10)
top_risk[["Borrower_ID","Income","Credit_Score","EMI","EMI_Ratio","Past_Defaults","Risk_Score","Current_Default"]].to_csv("top10_risk.csv", index=False)

print("Saved visuals and top10_risk.csv")
