names = {"Rahil", "Aaryan", "Baria", "Nirmit", "Aayush", "Dhyaan"}
a_names = set()
b_names = set()
for name in names:
    if name.startswith("A"):
        a_names.add(name)
    elif name.startswith("B"):
        b_names.add(name)
print(a_names)
print(b_names)

