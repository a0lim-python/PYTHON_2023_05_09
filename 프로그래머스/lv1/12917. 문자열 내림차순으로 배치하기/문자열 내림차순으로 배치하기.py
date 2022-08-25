# string.ascii_lower(upper)case & ''.join() & sorted

def solution(s):
    import string
    lower = ''; upper = ''
    
    for i in s:
        if s in string.ascii_lowercase:
            lower += i
        else:
            upper += i
            
    answer = ''.join(sorted(lower, reverse = True) + sorted(upper, reverse = True))
        
    return answer

# someone else's answer: ''.join(), sorted

def solution(s):
    return ''.join(sorted(s, reverse=True)) ## 기본 sorted 순서: 대문자 A-Z, 소문자 a-z
