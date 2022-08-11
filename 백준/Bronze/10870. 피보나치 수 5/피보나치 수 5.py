# 재귀
n = int(input())

def fib(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
        
print(fib(n))

# for loop
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
