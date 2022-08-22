# pop

def solution(n):
    ans = list(str(n)) ## int 형태로는 list 변환 불가능
    answer = []
    for i in range(len(ans)):
        answer.append(int(ans.pop()))
    return answer
