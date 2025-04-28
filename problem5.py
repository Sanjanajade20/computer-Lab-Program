lst=[(3,5),(),(),(5,4,3,),(6,5,4,),(),(),(),(10,)]
ls1=[]
for i in lst:
    if len(i)!=0:
        ls1.append(i)
print(ls1)
'''
another method
if i:
    ls1.append(i)
'''
# Output: [(3, 5), (5, 4, 3), (6, 5, 4), (10)]