def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

## 재귀
def solution(a, b):
    
    def dot(a, b, i = 0, ans = 0):
        if i == len(a): ## 중지 조건
            return ans
        else:
            ans += a[i] * b[i]
            i += 1
            return dot(a, b, i = i, ans = ans)

    answer = dot(a, b)
    return answer
