import string

word = input()
word = word.upper()
unique = list(set(word))

cnts = []

for i in range(0,len(unique)):
    cnts.append(word.count(unique[i]))

max = max(cnts)
if cnts.count(max)!= 1: ## several maxs
    print('?')
else:
    print(unique[cnts.index(max)])