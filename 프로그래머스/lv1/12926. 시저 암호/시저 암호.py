# string.ascii_upper(lower)case & index

def solution(s, n):
    import string
    
    s = list(s)
    up = string.ascii_uppercase; low = string.ascii_lowercase

    for i in range(len(s)):
        if s[i] in up:
            s[i] = (up * 2)[up.index(s[i]) + n] ## z 이상으로 넘어가는 경우를 위해, up * 2로 리스트 붙임
        elif s[i] in low * 2:
            s[i] = (low * 2)[low.index(s[i]) + n]
            
    answer = ''.join(s)
    return answer
