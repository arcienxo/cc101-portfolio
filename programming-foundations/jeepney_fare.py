#jeepney_fare.py
distance = int(input("Distance: "))
discount = input("Discount? (Y/N): ")
if distance <= 4:
    fare = 13.00
else:
    extra_km = distance - 4
    fare = 13.00 + (extra_km * 1.80)

if discount == "Y":
    fare = fare * 0.80
print(f"Fare: PHP {fare:.2f}")