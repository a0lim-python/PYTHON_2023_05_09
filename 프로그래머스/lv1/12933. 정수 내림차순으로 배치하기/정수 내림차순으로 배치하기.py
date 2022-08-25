def solution(n):
    answer = 0
    n = sorted(str(n), reverse = True)
    answer = int(''.join(n))
    return answer