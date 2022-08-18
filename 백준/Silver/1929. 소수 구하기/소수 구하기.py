import math
M, N = map(int, input().split())

def primes(n: int):
    
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False
    answer = []
    if n >= 2:
        for i in range(2, n+1):
            if arr[i] is True:
                answer.append(i)
                j = 2
                while i * j <= n:
                    arr[i * j] = False
                    j += 1
    return answer
                
for i in primes(N):
    if i >= M:
        print(i)