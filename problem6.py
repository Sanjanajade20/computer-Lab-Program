def replace(lst):
    if lst == []:
        return []
    return [0 if lst[0] < 0 else lst[0]] + replace(lst[1:])

lst = list(map(int, input().split()))
print(replace(lst))
