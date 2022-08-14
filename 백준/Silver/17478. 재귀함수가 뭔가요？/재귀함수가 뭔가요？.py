# 재귀 & 투 포인터
N = int(input())

first = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
ask = '"재귀함수가 뭔가요?"'
story1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
story2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
story3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
answer = '"재귀함수는 자기 자신을 호출하는 함수라네"'
last = '라고 답변하였지.'

def recursive(N: int, m = 0, n = 2 * N):
    ## m: story start pointer, n: answer pointer
    if m < 0 or n < -1: ## 종료 조건
        return
    else: 
        if m == 0: ## print once
            print(first)

        if m < n:
            print('____' * m + ask)
            print('____' * m + story1)
            print('____' * m + story2)
            print('____' * m + story3)
        elif n == m:
            print('____' * m + ask)
            print('____' * m + answer)
        else:
            print('____' * (n+1) + last)
        
        return recursive(N, m + 1, n - 1)
        
recursive()


# 재귀
N = int(input())

first = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
ask = '"재귀함수가 뭔가요?"'
story1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
story2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
story3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
answer = '"재귀함수는 자기 자신을 호출하는 함수라네"'
last = '라고 답변하였지.'

def story(N: int, num=1): # 처음 num = 1 / 이후 재귀호출로 1씩 증가
    if num > N:
        return
    elif num <= N:
        print('____' * (num-1) + ask)
        print('____' * (num-1) + story1)
        print('____' * (num-1) + story2)
        print('____' * (num-1) + story3)
        return story(N, num+1)

def last_answer(N: int):
    if N < 0:
        return
    else:
        print('____' * N + last)
        return last_answer(N - 1)

print(first)
story(N)
print('____' * N + ask)
print('____' * N + answer)
last_answer(N) # 구문을 나누어 def를 만들고 순서에 맞게 print함


# for loop
cnt = int(input())

first = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
ask = '"재귀함수가 뭔가요?"'
story1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n'
story2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n'
story3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
answer = '"재귀함수는 자기 자신을 호출하는 함수라네"'
last = '라고 답변하였지.'

def ask_answer(cnt: int):
    if cnt <= 50 and cnt >= 1:
        print(first)
        for i in range(0,cnt):    
            print('____' * i + ask + '\n' + '____' * i + story1 + '____' * i + story2 + '____' * i+ story3)
        print('____'* cnt + ask)
        print('____'* cnt + answer)
        for i in range(cnt,-1,-1):    
            print('____' * i + last)

ask_answer(cnt)
