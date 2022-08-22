# collections.Counter + set + 2 case

def solution(participant, completion, answer = None):
    import collections
    if set(participant) != set(completion): ## 비완주자가 동명이인이 아닌 경우
        answer = list(set(participant) - set(completion))[0]
    else: ## 비완주자가 동명이인인 경우
        ls = list(set(participant))
        p = collections.Counter(participant); c = collections.Counter(completion)
        for i in ls:
            if p[i] != c[i]:
                answer = i
                break   
    return answer

# collections.Counter: 비완주자가 동명이인인 경우에 for 문을 돌리기 때문에, 두 경우 모두 한 번에 판별

def solution(participant, completion):
    import collections

    ls = list(set(participant))
    p = collections.Counter(participant); c = collections.Counter(completion)
    for i in ls:
        if p[i] != c[i] or c[i] == 0: ## 비완주자가 동명이인인 경우 / 아닌 경우
            answer = i
            break

    return answer

# someone else's answer: 

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion) ## collections.Counter에서 - 연산이 가능
    return list(answer.keys())[0]
