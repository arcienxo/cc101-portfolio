#buggy_tracker.py
count = 1
total = 0
while count <= 3:
    score = float(input("Enter score: "))
    total = total + int(score)
    count += 1

average = total / 3

if average >= 75:
    print("PASSED")
else:
    print("FAILED")
    print("Average: ", average)