# 재귀
N = int(input())
result = 1

def fact(num: int):
    if num == 0: ## 0! = 1 // 1 * 0 = 0
        return 1
    if num >= 1: ## 종료 조건: num < 1
        return(num * fact(num - 1)) ## num -= 1

print(fact(N))


# for loop
n = int(input())

def fact(N):
    result = 1
    for i in range(1,N+1):
        result *= i
    print(result)
    
fact(n)
