# sqrt -> n의 값이 클수록 효율적

def solution(n):
    import math
    
    answer = 0
    for i in range(1, math.floor(math.sqrt(n))+ 1): ## 약수의 작은 값만 추출/더함 & 상대되는 약수 더함
        if n % i == 0:
            if i != n // i: ## 중복 제거
                answer += i + (n // i)
            else:
                answer += i
    return answer

# someone else's answer: n // 2 -> 중복 제거 불필요

def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0]) ## n의 절반만 추출: (1을 제외하고) 최소가 되는 약수 = 2 -> 최대 약수 = n // 2 -> 그 이상의 숫자는 약수가 될 수 없음
