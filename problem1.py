def count_lower_upper(s):
    d={}
    d["Upper"]=0
    d["lower"]=0
 
    for i in s:
        if i.islower():
            d["lower"]+=1

        elif i.isupper():
            d["Upper"]+=1
    return d
s1=input("Enter the string")
d1=count_lower_upper(s1)
print("Upper:-",d1["Upper"],"Lower:-",d1["lower"])