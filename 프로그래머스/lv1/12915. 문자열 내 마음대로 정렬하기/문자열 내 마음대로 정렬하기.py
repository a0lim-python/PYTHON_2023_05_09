def solution(strings, n):
    order = [n, range(1, 100)]
    strings.sort(key = lambda x: (x[n], x[:]))
    
    return strings
