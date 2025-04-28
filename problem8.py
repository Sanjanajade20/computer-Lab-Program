def recursive_length(s):
    if s == "":
        return 0
    return 1 + recursive_length(s[1:])

s = input()
print(recursive_length(s))