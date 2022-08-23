def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        measure = [i]
        for j in range(1, (i // 2) + 1):
            if i % j == 0:
                measure.append(j)
                
        if len(measure) % 2 == 0: ## 약수의 개수가 짝수
            answer += i
        else: ## 홀수
            answer -= i
        
    return answer