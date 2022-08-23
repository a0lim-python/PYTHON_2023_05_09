def solution(n, lost, reserve):
    i = 0
    reserve = sorted(reserve)
    while len(reserve) > 0:
        if i % 2 == 0: ## 앞부터 시작
            if reserve[0] in lost: ## 자신에게 빌려줌
                lost.remove(reserve[0])
            elif reserve[0] - 1 in lost: ## 왼쪽 학생에게 빌려줌
                lost.remove(reserve[0] - 1)
            elif reserve[0] + 1 in lost: ## 오른쪽 학생에게 빌려줌
                lost.remove(reserve[0] + 1)
                
            del reserve[0]
            i += 1

        else: ## 뒤쪽 시작
            if reserve[-1] in lost: ## 자신에게 빌려줌
                lost.remove(reserve[-1])
            elif reserve[-1] + 1 in lost: ## 오른쪽 학생에게 빌려줌
                lost.remove(reserve[-1] + 1)
            elif reserve[-1] - 1 in lost: ## 왼쪽 학생에게 빌려줌
                lost.remove(reserve[-1] - 1)
                
            del reserve[-1]
            i += 1
    
    return n - len(lost)
            
