def reverse_list(lst):
    if lst == []:
        return []
    return reverse_list(lst[1:]) + [lst[0]]

lst = list(map(int, input().split()))
print(reverse_list(lst))