num = int(input("input number:"))
if num < 0:
    print("Invalid")
elif num == 0:
    print(f'{num}! = 1')
else:
    giai_thua = 1
    for i in range(1,num+1):
        giai_thua *= i
    print(f'{num}! = {giai_thua}')
