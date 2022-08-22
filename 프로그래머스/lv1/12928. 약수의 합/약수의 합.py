def solution(n):
    import math
    
    answer = 0
    for i in range(1, math.floor(math.sqrt(n))+ 1):
        if n % i == 0:
            if i != n // i:
                answer += i + (n // i)
            else:
                answer += i
    return answer