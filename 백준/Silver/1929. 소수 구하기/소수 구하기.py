import math
M, N = map(int, input().split())

def primes(n: int):
    
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False
    answer = [] ## print primes
    if n >= 2: ## if n =1; range error
        for i in range(2, n+1):
            if arr[i] is True:
                answer.append(i) ## i: prime number
                j = 2 ## start to 2 (not include self)
                while i * j <= n:
                    arr[i * j] = False
                    j += 1
    return answer
                
for i in primes(N):
    if i >= M:
        print(i)
