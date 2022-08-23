# i // 2를 이용해 약수 구하기

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        measure = [i]
        for j in range(1, (i // 2) + 1):
            if i % j == 0:
                measure.append(j)
                
        if len(measure) % 2 == 0: ## 약수의 개수가 짝수
            answer += i
        else: ## 홀수
            answer -= i
        
    return answer

# someone else's answer: 제곱근이 정수인 경우, 약수의 개수는 홀수 개

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
