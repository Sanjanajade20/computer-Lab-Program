x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))
x3=int(input("Enter x3:"))
y3=int(input("Enter y3:"))
m1=(y2-y1)/(x2-x1)
m2=(y3-y2)/(x3-x2)
m3=(y3-y1)/(x3-x1)
if m1==m2==m3:
    print("colinear")
else:
    print("Not colinear")
