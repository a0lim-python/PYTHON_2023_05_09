def solution(n):
    ans = list(str(n))
    answer = []
    for i in range(len(ans)):
        answer.append(int(ans.pop()))
    return answer