N = int(input())
prime = list(map(int, input().split()))
prime_num = 0

def is_prime(n: int, i = 2, tf = 0):
    if n < 2 or i > n: ## 종료 조건
        return
    if n % i == 0:
        if i == n:
            tf = 1
            return tf
        else:
            return ## not prime
    return is_prime(n, i+1, tf)
 
for i in range(N):
    if is_prime(prime[i]) == 1:
        prime_num += 1
        
print(prime_num)