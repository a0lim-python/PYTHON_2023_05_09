import string
alphabet = list(string.ascii_uppercase) # list A-Z

word = input() # more than 1 char

sum = 0 ## answer

for i in range(0,len(word)): # each char
    index = alphabet.index(word[i]) # index of alphabet (A=0, B=1, ...)
    
    if index <= 14: ## A-O
        sum += index//3 + 3
    elif index >=15 and index <=18: ## PQRS
        sum+= 6 +2
    elif index >= 19 and index<=21: ## TUV
        sum+= 7 +2
    else: ## WXYZ
        sum+= 8 +2

print(sum)