# SOLVED 1
import string

S = input()
letters = string.ascii_lowercase
result = []

for i in range(len(letters)):
    result.append(S.find(letters[i]))

print(result)

# SOLVED 2
import string

S = input()
letters = string.ascii_lowercase

for i in range(len(letters)):
    if letters[i] in S:
        print(S.index(letters[i]))
    else:
       print(-1)
    

# NOT SOLVED
import string

word = list(input())

alphabet = list(string.ascii_lowercase)  ## a, b, c, ... ,z
result = [-1 for _ in range(0,len(alphabet))] ## default: -1

for i in range(0,len(result)):
    letter = word[i]
    result[alphabet.index(letter)] = word.index(letter)
 
print(result)
