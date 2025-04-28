def tup(n):
    t=()
    for i in range(1,n+1):
        t+=((i,i**2,i**3),)
    return t
n=int(input("Enter ending value:-"))
print(tup(n))