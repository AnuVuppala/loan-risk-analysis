# data_generator.py
import random
import csv

random.seed(42)
n = 500
with open("loan_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Borrower_ID","Age","Income","Credit_Score","Loan_Amount","EMI","Loan_Duration","Past_Defaults","Current_Default"])
    for i in range(1, n+1):
        age = random.randint(21, 60)
        income = random.randint(10000, 150000)  # monthly income
        credit = random.randint(300, 900)
        loan_amount = random.randint(20000, 1000000)
        duration = random.choice([12,24,36,48,60,72])
        # mock EMI roughly = loan_amount / duration / (1) + noise
        emi = int(loan_amount / duration / 1.0 + random.randint(-500, 500))
        past_defaults = random.choices([0,1,2], weights=[80,15,5])[0]
        # simple rule for default probability
        prob = 0.0
        if credit < 600: prob += 0.25
        if emi > 0.4 * income: prob += 0.35
        if past_defaults >= 1: prob += 0.25
        # cap prob to 0.9
        prob = min(prob, 0.9)
        default = 1 if random.random() < prob else 0
        writer.writerow([i, age, income, credit, loan_amount, emi, duration, past_defaults, default])
print("Generated loan_data.csv with", n, "rows")
