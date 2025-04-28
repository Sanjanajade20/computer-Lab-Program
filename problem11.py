x = float(input("Enter angle in degrees: "))
x = x * 3.14159 / 180  

sinx = 0
sign = 1
for i in range(10):  
    term = 1
    for j in range(1, 2*i+2):
        term *= x / j
    sinx += sign * term
    sign *= -1

print("sin(x) =", sinx) 