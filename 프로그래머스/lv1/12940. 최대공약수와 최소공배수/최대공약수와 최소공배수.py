def solution(n, m):
    import math
    
    def measure(n, m, i = 2, result = [1]):
        if n == 1 or m == 1:
            return result
        else:
            while n >= i and m >= i:
                if n % i == 0 and m % i == 0: # 공약수인 경우
                    result.append(i)
                    return measure(n // i, m // i, i = 2, result = result)
                else:
                    i += 1
            return result
                    
    answer = [0, 0]
    
    answer[0] = math.prod(measure(n, m))
    answer[1] = int(n * m / answer[0])

    return answer