def solution(survey, choices):
    answer = []
    pers = 'RTCFJMAN'
    pers_num = [0] * 4 ## 왼쪽 유형: 양수 / 오른쪽 유형: 음수로 표현
    point = list(range(3,-4,-1)) ## 3 ~ -3
    
    for i in range(len(survey)):
        idx = pers.index(survey[i][0]) # 해당하는 성격 유형: 왼쪽 알파벳
        if idx % 2 == 0:
            pers_num[int(idx // 2)] += point[choices[i] - 1] ## 홀수: 왼쪽 -> 양수
        else:
            pers_num[idx // 2] -= point[choices[i] - 1] ## 짝수: 오른쪽 -> 음수
            
    for i in range(len(pers_num)):
        if pers_num[i] >= 0: ## 사전식 순: R / C / J / A (왼쪽 유형) -> 값이 같은 경우에는 왼쪽 유형 선택
            answer.append(pers[2 * i])
        else:
            answer.append(pers[2 * i + 1])
            
    answer = ''.join(answer) ## list to str

    return answer
