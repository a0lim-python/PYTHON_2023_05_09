# SOLVED 1

import string

S = input()
letters = string.ascii_lowercase

for i in letters:
    print(S.find(i))  ## find // index_num or -1

print(result)


# SOLVED 2

import string

S = input()
letters = string.ascii_lowercase

for i in range(len(letters)):
    if letters[i] in S:
        print(S.index(letters[i])) ## index // index_num of ERROR
    else:
       print(-1)

#####################################################################
    
# NOT SOLVED
## result shouldn't a list
import string

word = list(input())

alphabet = list(string.ascii_lowercase)  ## a, b, c, ... ,z
result = [-1 for _ in range(0,len(alphabet))] ## default: -1

for i in range(0,len(result)):
    letter = word[i]
    result[alphabet.index(letter)] = word.index(letter)
 
print(result)
