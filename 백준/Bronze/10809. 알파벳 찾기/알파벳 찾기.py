import string

S = input()
letters = string.ascii_lowercase

for i in letters:
    print(S.find(i))