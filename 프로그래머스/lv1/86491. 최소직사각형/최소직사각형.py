def solution(sizes):
    m = [min(sizes[i]) for i in range(len(sizes))]
    M = [max(sizes[i]) for i in range(len(sizes))]
    answer = max(M) * max(m)
    return answer