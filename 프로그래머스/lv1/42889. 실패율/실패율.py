# set & count & sorted lambda

def solution(N, stages):
    
    fail = [] ## 실패율
    for i in range(1, N + 1):
        if i not in list(set(stages)): # stages에 없다면 실패율 = 0(모두 성공)
            fail.append(0)
        else:
            fail.append(stages.count(i)/len(stages))
            stages = [j for j in stages if j > i] # 해당 스테이지 사람들 삭제
        
    answer = sorted(list(enumerate(fail)), key = lambda x: (-x[1], x[0])) ## 실패율 낮은 순, 스테이지 단계가 낮은 순으로 정렬
    answer = [answer[i][0] + 1 for i in range(N)]
        
    return answer
