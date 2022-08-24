# 재귀함수(recursive function) & math.prod & A * B = GCD * LCM

def solution(n, m):
    import math
    
    def measure(n, m, i = 2, result = [1]): ## 공약수들을 추출
        if n == 1 or m == 1: ## 1인 경우, 최대공약수 = 1
            return result
        else:
            while n >= i and m >= i:
                if n % i == 0 and m % i == 0: ## 공약수인 경우
                    result.append(i)
                    return measure(n // i, m // i, i = 2, result = result) ## 재귀
                else:
                    i += 1
            return result
                    
    answer = [0, 0]
    
    answer[0] = math.prod(measure(n, m)) 
    answer[1] = int(n * m / answer[0]) ## LCM = n * m / GCD

    return answer

# someone else's answer: 유클리드 호제법
'''
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

참고: https://velog.io/@jwisgenius/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98
'''

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
