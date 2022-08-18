def primes(n: int):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False
    answer = []
    
    if n >= 2:
        for i in range(2, n+1):
            if arr[i] == True:
                answer.append(i)
                j = 2
                
                while i * j <= n:
                    arr[i * j] = False
                    j += 1
    elif n == 1:
        answer = [1]
    return answer

while True:
    cnt = 0
    n = int(input())
    if n >= 1:
        for p in primes(2 * n):
            if p > n and p <= 2 * n:
                cnt += 1
        print(cnt)
    else:
        break