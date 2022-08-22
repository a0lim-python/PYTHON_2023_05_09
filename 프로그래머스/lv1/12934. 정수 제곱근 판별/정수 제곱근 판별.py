def solution(n):
    import math
    
    nn = math.sqrt(n)
    
    if math.floor(nn) == math.ceil(nn): ## 올림과 내림 값이 같음 -> 정수
        answer = (nn + 1) ** 2
    else:
        answer = -1
        
    return answer