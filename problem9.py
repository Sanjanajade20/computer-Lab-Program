list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

difference = [x for x in list1 if x not in list2]
print("Elements in list1 not in list2:", difference)