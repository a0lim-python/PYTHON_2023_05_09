# 소수찾기 2: for loop
N = int(input())
prime = list(map(int, input().split()))
prime_num = 0

def is_prime(n: int):
    if n < 2:
        return False
    else: 
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

for p in range(N):
    if is_prime(prime[p]) == True:
        prime_num += 1

print(prime_num)