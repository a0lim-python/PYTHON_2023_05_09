n = int(input())

def number_of_sequence(n):
    cnt = 0 ## # of sequence
    
    for j in range(1,n+1): ## all numbers equeal or smaller than n
        diff_list = []
        
        if j < 10:
            cnt+=1
        else:
            #j=1000
            for i in range(0,len(str(j))-1):
                #i=1
                diff = int(str(j)[i])-int(str(j)[i+1]) ## diff between each number
                diff_list.append(diff)

            if len(set(diff_list)) == 1: ## every diff is same -> count it as sequence
                cnt+=1
    result = cnt        
    return result


print(number_of_sequence(n))
