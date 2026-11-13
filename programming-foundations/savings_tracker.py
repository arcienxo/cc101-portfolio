#savings_tracker.py
total = 0
days = 0

amount = float(input("Savings today: "))

while amount != 0:
    total += amount
    days += 1

    amount = float(input("Savings today: "))

print(f"Total saved in {days} days: {total:,.2f}")