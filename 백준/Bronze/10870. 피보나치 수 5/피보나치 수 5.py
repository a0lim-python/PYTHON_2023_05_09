num = int(input())

def fib(n):
    result = [0, 1]
    if n == 0:
        print(0)
    else:
        for i in range(n-1):
            result.append(sum(result))
            del result[0]
        print(result[-1])
    
fib(num)