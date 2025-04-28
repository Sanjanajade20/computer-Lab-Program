import math
x=int(input("Enter x coordinate of center:"))
y=int(input("Enter y coordinate of center:"))
r=float(input("enter the radius:-"))
a=int(input("Enter x coordinate of center:"))
b=int(input("Enter y coordinate of center:"))

distance= math.sqrt((x-a)**2+(y-b)**2)

if distance<r :
    print("point is inside the circle")
elif distance==r:
    print("point is on the circle")
else:
    print("point is outside the circle")

