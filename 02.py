#large and smallest of three values
def ls3():
    a=int(input("Enter a number-1 = "))
    b=int(input("Enter a number-2 = "))
    c=int(input("Enter a number-3 = "))
    if a>b:
        if a>c:
            if b>c:
                print(a,">",b,">",c)
            elif c>b:
                print(a,">",c,">",b)
            else:
                print(a,">",b,"=",c)
        elif c>a:
            print(c,">",a,">",b)
    elif b>a :
        if b>c:
            if a>c:
                print(b,">",a,">",c)
            elif c>a:
                print(b,">",c,">",a)
            else:
                print(b,">",a,"=",c)
        elif c>b:
            print(c,">",b,">",a)
    elif a==b :
        if c>a:
            print(c,">",a,"=",b)
        elif c<a:
            print(a,"=",b,">",c)
        else:
            print(a,"=",b,"=",c)

ls3()
ls3()
ls3()
