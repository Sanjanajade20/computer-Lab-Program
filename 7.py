
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

nCr = factorial(n) // (factorial(r) * factorial(n - r))

nPr = factorial(n) // factorial(n - r)

print(f"{n}C{r} = {nCr}")
print(f"{n}P{r} = {nPr}")
