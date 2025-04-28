a=int(input("Enter length:"))
b=int(input("Enter breath:"))
p=2*(a+b)
r=a*b
if r>p:
    print("area > perimeter")
elif r<p:
    print("area < perimeter")
else:
    print("area = perimeter")
