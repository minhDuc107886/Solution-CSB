num = int(input("Input number:"))
num = str(num)
sum = 0
for i in num:
    sum += int(i)
print(f"Sum of digits of {num}: {sum}")
