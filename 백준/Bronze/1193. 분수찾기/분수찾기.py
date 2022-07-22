X = int(input()) ## num

num_direction = [1] ## antidiagonal of [n,n]
accum = 1 ## accumulate 0 to n

while X > accum+num_direction[-1]: ## while X > accum+num_direction[-1]
        num_direction.append(num_direction[-1] + 1)
        accum += num_direction[-1]

else: ## last antidiagonal
    ## last direction : even (default)
    if X == accum: ## no left
        answer = [num_direction[-1],1]
    else: ## There are left
        answer = [num_direction[-1]+1,1] ## start position
        for i in range(0,X-accum-1):
            answer[0] -= 1
            answer[1] += 1

    if num_direction[-1]%2 == 1: ## last direction : odd
        answer = [answer[1],answer[0]] ## start position
            
print(str(answer[0])+"/"+str(answer[1]))