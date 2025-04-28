def fact(n):
    m = 1
    while(n > 0):
        m = m * n
        n -= 1
    return m

n = float(input("Enter a value for theta in radians: "))
i = 1
sum = 0
threshold = 1e-10  
term = n**(2*i-1) / fact((2*i-1))

while(abs(term) > threshold): #here abs() term is use for absolute value
    if(i % 2 == 0):
        sum -= term
    else:
        sum += term
    i += 1
    term = n**(2*i-1) / fact((2*i-1))

print(sum)
