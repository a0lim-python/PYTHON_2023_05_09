cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in range(len(cro)):
    word = word.replace(cro[i], '*')
print(len(word))


## NOT SOLVED
import re

word = input()

word = re.sub('dz|lj|nj', 'A', word)
word = re.sub('-|=', '', word)

print(len(word))
