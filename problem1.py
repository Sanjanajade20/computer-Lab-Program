import random

odd_nus = [random.randrange(1, 100, 2) for _ in range(5)]
print("Original odd numbers:", odd_nus)

even_nus = [random.randrange(0, 100, 2) for _ in range(4)]
print("Even numbers:", even_nus)

odd_nus[2] = even_nus
print("After replacement:", odd_nus)

flat_lst = []
for item in odd_nus:
    if isinstance(item, list):
        flat_lst.extend(item)
    else:
        flat_lst.append(item)
print("Flattened list:", flat_lst)

flat_lst.sort()
print("Final sorted list:", flat_lst)