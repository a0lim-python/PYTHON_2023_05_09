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
