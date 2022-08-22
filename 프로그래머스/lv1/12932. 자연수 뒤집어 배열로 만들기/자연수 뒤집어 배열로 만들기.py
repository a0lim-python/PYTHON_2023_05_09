# pop

def solution(n):
    ans = list(str(n)) ## int 형태로는 list 변환 불가능
    answer = []
    for i in range(len(ans)):
        answer.append(int(ans.pop()))
    return answer

# someone else's answer 1: reversed

def solution(n):
    return list(map(int, reversed(str(n)))) ## reversed: str 뒤집기

# someone else's answer 2: [::-1]

def solution(n):
    n = str(n)[::-1] ## str[::-1]: str 뒤집기
    answer = list(map(int, n))
    return answer
