# 1) Input income and calculate tax:
# • ≤2,50,000 → No tax.
# • 2,50,001 – 5,00,000 → 5% tax.
# • 5,00,001 – 10,00,000 → 20% tax.
# • Above 10,00,000 → 30% tax.

income = float(input("Enter your income: "))

if income <= 250000:
    tax = 0
    print("No tax.")

elif income <= 500000:
    tax = income * 0.05
    print("Tax at 5% =", tax)

elif income <= 1000000:
    tax = income * 0.20
    print("Tax at 20% =", tax)

else:
    tax = income * 0.30
    print("Tax at 30% =", tax)

print("Total calculated tax is: ", tax)