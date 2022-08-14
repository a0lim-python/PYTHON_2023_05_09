def solution(s):
    import re
    
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(eng)):
        if s.count(eng[i]) > 0:
            s = re.sub(eng[i], str(i), s)
                
    answer = int(s)
    return answer