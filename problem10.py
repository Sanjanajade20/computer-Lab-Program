list1 = list(range(1, 7))
list2 = list(range(6, 0, -1))
result = list(map(lambda x, y: x + y, list1, list2))
print(result)

