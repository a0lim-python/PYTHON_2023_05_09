N = int(input())
words = [input() for i in range(0,N)]  ## enter input
counts = 0 ## answer


for i in range(0,N):
    word_1 = words[i] ## word_1 = "happy"
    word_1 = word_1 + '*' ## word_1 = "happy*"
    dup_del = []
    
    for j in range(0,len(word_1)-1): # ['y', 'p', 'a', 'h'] => 4
        if word_1[j] != word_1[j+1]:
            dup_del.append(word_1[j])
    if len(list(set(word_1)))-1 == len(dup_del):
        counts += 1
        
print(counts)