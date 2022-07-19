####### code 1 => run time error

N = int(input())

words = [input() for i in range(0,N)]  ## enter input
counts = 0 ## answer

for i in range(0,N):
    word_1 = words[i] ## word_1 = "happy"
    unique = list(set(word_1)) ## unique = ['y', 'p', 'a', 'h']
    
    for j in range(0,len(unique)): ## 'y'
        if word_1.count(unique[j])>1: ## loop when index is more than 1
            index = []

            index.append([k for k in range(0,len(word_1)) if word_1[k]==unique[j]])
            index = sum(index, []) ## delete doble list
            
            gap = []
            gap.append([index[g]-index[g+1] for g in range(len(index)-1)])
            gap = sum(gap, [])
            
        if len(gap) - gap.count(-1) == 0:
            counts += 1
                
print(counts)
            
############# code 2 => success

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
