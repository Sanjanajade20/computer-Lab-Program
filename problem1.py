namelist=[ "Alice" , ("Rohan",) , "Chlaire" , ("Ravi",) , "Sita", ("Ram",) ]
boys=0
girls=0
for name in namelist:
    if isinstance(name,tuple):
        boys+=1
    else:
        girls+=1
print("number of boys",boys)
print("number of girls",girls)