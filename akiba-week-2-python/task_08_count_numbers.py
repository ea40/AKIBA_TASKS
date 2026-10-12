
even = 0
odd = 0
zero = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    elif i % 2 != 0:
        odd += 1
    else:
        zero += 1


values = list(map(int, input("Enter numbers separated by spaces: ").split()))
positive, negative, zero = count_numbers(values)

print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zero numbers: {zero}")

