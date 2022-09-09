MDY = input("Date in MM/DD/YYYY format: ")
# c1
print(f"Date in DD/MM/YYYY format: {MDY[3:5]}/{MDY[0:2]}/{MDY[6:]}")
# c2
x = MDY.split('/')
print(type(x))
print(f"Date in DD/MM/YYYY format:{x[1]}/{x[0]}/{x[2]}")