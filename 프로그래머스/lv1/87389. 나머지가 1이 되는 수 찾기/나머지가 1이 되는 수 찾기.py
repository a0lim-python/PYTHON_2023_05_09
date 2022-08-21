def solution(n):
    # answer: (n-1)의 min(최대 공약수)
    result = 2
    while (n-1) % result != 0:
        result += 1
    answer = result
    return answer