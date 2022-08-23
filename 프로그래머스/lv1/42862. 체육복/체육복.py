# while & 투 포인터

def solution(n, lost, reserve):
    i = 0 ## 포인터 선택 지표
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
            
# someone else's answer

def solution(n, lost, reserve):
    reserve = sorted(reserve)
    _reserve = [r for r in reserve if r not in lost] ## 자기 자신에게 빌리는 경우 삭제
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1 ## 왼쪽, 오른쪽 순서로 삭제
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
