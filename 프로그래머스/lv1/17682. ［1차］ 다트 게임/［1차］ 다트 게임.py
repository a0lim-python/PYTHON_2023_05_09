#  try/except & for

def solution(dartResult):
    dart = []
    for i in range(len(dartResult)):
        try: ## 점수(int)
            if dartResult[i] == '0' and dartResult[i - 1] == '1': ## 10인 경우
                dart[-1] *= 10
            else:
                dart.append(int(dartResult[i]))
        except: ## 그 외(str)
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

# someone else's answer 1: replace, if else

def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult] ## 10을 k로 변환 후 다시 10으로 저장 -> 1, 0으로 나뉘지 않게 방지
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1) ## bonus를 index에 맞게 처리
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else: ## 숫자인 경우 append
            answer.append(int(j))
            i += 1 ## 숫자 입력 후 0으로 시작
    return sum(answer)

# soneone else's answer 2: 정규표현식(re.complie), findall

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)') ## 점수, bonus, 옵션으로 나눔 ## \d+: 숫자(\d) 1번 이상 반복(+) ## [SDT]: S or D or T ## [*#]?: *이나 #중 하나(?: 아예 없거나 1개만 있을 때만 return)
    dart = p.findall(dartResult) ## // [('1', 'D', ''), ('2', 'S', ''), ('0', 'T', '')]
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0: ## 이전 점수에 적용
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]] ## 한번에 계산(option이 없는 경우도 포함)

    answer = sum(dart)
    return answer
