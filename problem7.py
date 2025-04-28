def recursive_avg(lst):
    def helper(index):
        if index == len(lst):
            return (0, 0)
        s, count = helper(index + 1)
        return (lst[index] + s, 1 + count)
    total, cnt = helper(0)
    return total / cnt if cnt != 0 else 0

lst = list(map(float, input().split()))
print(recursive_avg(lst))