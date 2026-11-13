#sum_to_n.py
num = int(input("Enter a positive number: "))
total = 0

for i in range(1, num + 1):
    total += i

print(f"Sum of 1 to {num} = {total}")