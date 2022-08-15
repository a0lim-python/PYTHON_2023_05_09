# 소수 찾기 1: 재귀함수
## O(n)
### 종료 조건과 추가 변수 생성(i, tf)으로 인한 비효율성 있음

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


# 소수찾기 2: for loop
### n 이전까지 모든 수를 넣어야 하는 비효율성 있음
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


# 소수찾기3: 제곱근
## O(n/2)
### 약수의 대칭성(16의 약수는 1, 2, 4, 8, 16)을 이용해 소수찾기 2 방법의 절반 정도만 loop를 돌림
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
