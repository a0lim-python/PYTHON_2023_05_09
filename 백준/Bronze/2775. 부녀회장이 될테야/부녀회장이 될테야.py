from itertools import accumulate

T = int(input()) ## test case

for i in range(T):
    k = int(input()) ## floor ## k=3
    n = int(input()) ## number of room ## n=4
    before_k = list(range(1,n+1)) ## [1,2,3,4]

    for k_num in range(1,k+1):
        current_k = list(accumulate(before_k)) ## 누적합 
        if k_num != k+1: ## continue until k-th floor
            before_k = current_k        

    print(current_k[-1]) ## print k-th floor n-th room