# Create three dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Concatenate them to create fourth dictionary
d4 = {}
d4.update(d1)
d4.update(d2)
d4.update(d3)

print("Fourth dictionary:", d4)
#Another way
d4={**d1,**d2,**d3}
print("Fourth dictionary:", d4)