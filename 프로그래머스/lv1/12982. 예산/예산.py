def solution(d, budget):
    if sum(d) <= budget:
        answer = len(d)
    else:
        d = sorted(d)
        while sum(d) > budget:
            d.pop()
        answer = len(d)
    
    return answer