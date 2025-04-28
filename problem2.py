def is_dict_empty(d):
    return not bool(d)

d1 = {}
d2 = {'a': 1}

print("Is dict1 empty?", is_dict_empty(d1))
print("Is dict2 empty?", is_dict_empty(d2))