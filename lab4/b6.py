from turtle import *
num = int(input("Input number of edges: "))
ang  = (num -2)*180/num

for i in range(num):
    forward(90)
    right(180-ang)
done()