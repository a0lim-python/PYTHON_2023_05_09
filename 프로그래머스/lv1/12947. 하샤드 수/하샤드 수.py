# sum & map & list & str

def solution(x):
    if x % sum(list(map(int,list(str(x))))) == 0:
        answer = True
    else:
        answer = False
    return answer
