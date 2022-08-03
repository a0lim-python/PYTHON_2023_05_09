cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in range(len(cro)):
    word = word.replace(cro[i], '*')
print(len(word))