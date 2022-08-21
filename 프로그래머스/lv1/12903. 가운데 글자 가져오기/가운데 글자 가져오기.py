def solution(s):
    if len(s) % 2 == 1: ## 홀수
        i = len(s) // 2 ## len = 5; 2 = 5 // 2
        answer = s[i]
    else: ## 짝수
        i = len(s) // 2 ## len = 4; 1:2 -> 2 = 4 // 2
        answer = s[i - 1:i + 1]
    return answer