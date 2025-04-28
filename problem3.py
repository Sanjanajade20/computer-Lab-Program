def cnt_vowel(s):
    vowel = "aeiouAEIOU"
    if s == "":
        return 0
    return (s[0] in vowel) + cnt_vowel(s[1:])

s = input()
print(cnt_vowel(s))