from turtle import *

shape('turtle')

# draw the curve
radius = 1
for i in range(15):  
  circle(radius, 180)
  radius += 10

mainloop()