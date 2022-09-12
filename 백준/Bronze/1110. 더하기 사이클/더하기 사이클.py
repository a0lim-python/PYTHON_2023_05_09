N = int(input())
n = N
count = 0

while True:
    if n < 10:
        n = n * 11 ## 9 -> 99
    else:
        n = int(str(n % 10)[-1] + str((n // 10)+ (n % 10))[-1])
    count += 1
    
    if n == N:
        break

print(count)