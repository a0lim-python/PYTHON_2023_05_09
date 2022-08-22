# pop

def solution(d, budget):

    d = sorted(d)
    while sum(d) > budget:
        d.pop()
    answer = len(d)
    
    return answer
