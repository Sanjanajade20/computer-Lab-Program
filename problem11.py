import random
lst = random.sample(range(-15, 16), 10)
squares = list(map(lambda x: x * x, lst))
print(lst)
print(squares)

