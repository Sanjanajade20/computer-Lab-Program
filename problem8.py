n=int(input("enter the value of n"))
temp=1
for i in range(1,n+1):
    temp=((n-i)+1)*temp
print(temp)