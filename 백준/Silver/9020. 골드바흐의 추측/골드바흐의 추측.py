import math

num = int(input())

def is_prime(n: int):
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
    start = int(math.floor(n / 2))   
    while start > 0:
        if is_prime(start) == True:
            if is_prime(n - start) == True:
                print(start, n - start)
                break
            else:
                start -= 1
        else:
            start -= 1