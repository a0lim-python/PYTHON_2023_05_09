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
    start = int(math.floor(n / 2)) ## n is sum of two number -> try half of n, then try other half   
    while start > 1:
        if is_prime(start) == True: ## if number 1 is prime;
            if is_prime(n - start) == True: ## if number 2 is prime;
                print(start, n - start) ## start < n - start (not need sort)
                break
            else:
                start -= 1 ## froma mean to 2
        else:
            start -= 1
