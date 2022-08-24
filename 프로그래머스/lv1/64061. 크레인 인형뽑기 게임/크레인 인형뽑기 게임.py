# zip & remove(0)
## numpy를 사용하지 않음
def solution(board, moves):
    answer = 0
    basket = []
    board = list(map(list,(zip(*board)))) ## 행렬 전환(형태: 리스트)
    
    for i in range(len(board)): ## 0 제거
        while board[i][0] == 0:
            board[i].remove(0)
    
    for i in moves:
        if board[i - 1] != []:
            basket.append(board[i - 1][0]) ## 위에 있는 인형을 basket으로 이동
            del board[i - 1][0]
        
        if len(basket) > 1:
            if basket[-1] == basket[-2]: ## 같은 인형이 쌓이면 바구니에서 삭제
                basket = basket[:-2]
                answer += 2 ## 사라진 인형의 수
    
    return answer

# somone else's answer: 이중 for & pop()
def solution(board, moves):
    stacklist = [] ## basket과 같은 역할
    answer = 0

    for i in moves:
        for j in range(len(board)): ## 이중 for loop을 이용해 전체를 순환
            if board[j][i-1] != 0: ## 0인 경우는 스킵
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1) ## basket = basket[:-2]과 같은 역할
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
