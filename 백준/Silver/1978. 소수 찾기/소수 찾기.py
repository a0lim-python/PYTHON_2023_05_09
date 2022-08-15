# 소수찾기3: 제곱근
## O(n/2)
import math

N = int(input())
prime = list(map(int, input().split()))
prime_num = 0

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1): ## 제곱근까지만 나누기(이전에 없으면 이후에도 없음)
        if n % i == 0:
            return False
    return True

for p in range(N):
    if is_prime(prime[p]) == True:
        prime_num += 1

print(prime_num)