n = int(input("enter a number :"))
def fibo(n):
    a=1
    b=1
    while(n>0):
        c=a+b
        print(c)
        a=b
        b=c
        n-=1
fibo(n)
