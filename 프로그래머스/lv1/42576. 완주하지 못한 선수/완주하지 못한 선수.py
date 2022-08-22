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

