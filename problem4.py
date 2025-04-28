from operator import itemgetter
ls1=[("Pizza",100),("Noodles",90),("Burger",80),("Pasta",95),("Salad",85)]
sortedfood=sorted(ls1,key=itemgetter(1),reverse=True)
print(ls1)