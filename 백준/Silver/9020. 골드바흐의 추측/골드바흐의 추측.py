## 1. is_prime & root & loop half of n

import math

num = int(input())

def is_prime(n: int): ## prime number: True
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
            
for i in range(0,num):
    n = int(input())
    start = int(math.floor(n / 2)) ## n is sum of two number -> try half of n, and then try other half   
    while start > 1:
        if is_prime(start) == True: ## if number 1 is prime;
            if is_prime(n - start) == True: ## if number 2 is prime;
                print(start, n - start) ## start < n - start (not need sort)
                break
            else:
                start -= 1 ## from mean to 2
        else:
            start -= 1

## 2. Eratosthenes & try half of n ## timeout
num = int(input())

def primes(m: int): ## Eratosthenes
    arr = [True] * (m + 1)
    arr[0] = False ## 0, 1 is not prime number
    arr[1] = False
    answer = []
    
    for i in range(2, m + 1):
        if arr[i] == True:
            answer.append(i)
            j = 2
            
            while i * j <= m:
                arr[i * j] = False
                j += 1
                
    return answer

for i in range(0, num):
    n = int(input())
    p = primes(n) ## primes list
    
    mean_p = [j for j in p if j >= n / 2] ## prime numbers: start from mean to last prime number
    s = 0 ## temp num
    while True:
        if n - mean_p[s] in p:
            print(n - mean_p[s], mean_p[s])
            break
