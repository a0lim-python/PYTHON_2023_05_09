def solution(dartResult):
    dart = []
    for i in range(len(dartResult)):
        try:
            num = int(dartResult[i])
            if dartResult[i] == '0' and dartResult[i - 1] == '1': ## 10인 경우
                dart[-1] *= 10
            else:
                dart.append(num)
        except:
            ## bonus: 'S', 'D', 'T'
            if dartResult[i] == 'D':
                dart[-1] **= 2
            elif dartResult[i] == 'T':
                dart[-1] **= 3
            ## option: '*', '#'
            elif dartResult[i] == '*':
                dart[-1] *= 2
                if len(dart) > 1:
                    dart[-2] *= 2
            elif dartResult[i] == '#':
                dart[-1] *= -1
    answer = sum(dart)
    return answer