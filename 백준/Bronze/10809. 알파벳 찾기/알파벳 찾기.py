import string

S = input()
letters = string.ascii_lowercase

for i in range(len(letters)):
    if letters[i] in S:
        print(S.index(letters[i]))
    else:
       print(-1)