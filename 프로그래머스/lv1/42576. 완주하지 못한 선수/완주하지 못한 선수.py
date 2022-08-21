def solution(participant, completion,answer = None):
    import collections

    participant = collections.Counter(participant)
    completion = collections.Counter(completion)
    
    p_most = sorted(participant.most_common())
    c_most = sorted(completion.most_common())
    
    for i in range(len(c_most)):
        if p_most[i] != c_most[i]:
            answer = p_most[i][0]
            break
    if answer is None:
        answer = p_most[-1][0]
    
    
    return answer

