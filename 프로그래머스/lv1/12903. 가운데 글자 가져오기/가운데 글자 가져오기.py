def solution(s):
    if len(s) % 2 == 1: ## 홀수
        i = len(s) // 2 ## len = 5; 2 = 5 // 2
        answer = s[i]
    else: ## 짝수
        i = len(s) // 2 ## len = 4; 1:2 -> 2 = 4 // 2
        answer = s[i - 1:i + 1]
    return answer

# someone else's answer
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
