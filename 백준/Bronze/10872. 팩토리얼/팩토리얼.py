n = int(input())

def fact(N):
    result = 1
    for i in range(1,N+1):
        result *= i
    print(result)
    
fact(n)