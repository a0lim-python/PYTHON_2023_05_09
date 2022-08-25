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

# someone else's answer

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator ## dict로 저장 -> key: 단계, value: 실패율 => enumerate, answer[i][0] + 1 필요 없음
            denominator -= count ## 남은 사람의 수
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True) ## vakye(실패율)로 정렬 / 파이썬 3.7부터 dictionary의 순서 보장 -> 스테이지 단계 순서 고려 필요 없음
