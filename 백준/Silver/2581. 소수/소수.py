import math

M = int(input())
N = int(input())

def is_prime(n: int):
    arr = [True] * (n+1)
    arr[0] = False; arr[1] = False
    
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i] == True:
            j = 2
            
            while (i * j) <= n:
                arr[i * j] = False
                j += 1
    return arr

max = is_prime(N)

primes = [] ## prime keys list
for i in range(M, N + 1): ## from M to N
    if max[i] == True: ## prime key
        primes.append(i)

if len(primes) == 0: ## there is no prime key
    print(-1)
else:
    print(sum(primes)) ## sum
    print(primes[0]) ## min