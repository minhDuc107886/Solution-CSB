n = 0
num = 1000
print("Numbers with sum of digits = 9: ",end="")
while n < 10:
    sum = 0
    for i in str(num):
        sum += int(i)
    if sum == 9:
        n+=1
        print(num,end=" ")
    num += 1 
