import random
num_set = set(random.sample(range(15, 46), 10))
count = 0
for x in num_set:
    if x < 30:
        count += 1
print(count)
to_remove = set()
for x in num_set:
    if x > 40:
        to_remove.add(x)
for x in to_remove:
    num_set.remove(x)
print(num_set)

