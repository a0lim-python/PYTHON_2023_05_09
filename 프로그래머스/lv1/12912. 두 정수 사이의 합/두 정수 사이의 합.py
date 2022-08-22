## min/max + range
def solution(a, b):
    lst = list(range(min(a, b),max(a, b)+ 1))
    return sum(lst)
