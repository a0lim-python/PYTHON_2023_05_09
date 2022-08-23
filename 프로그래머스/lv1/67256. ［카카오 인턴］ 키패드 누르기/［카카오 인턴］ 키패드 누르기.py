def coor(num): ## 키패드의 숫자의 위치 좌표 (1,1) ~ (3,4) / coor(1) = (1,1)
    coor = [0, 0]
    
    if num == 0:
        coor = [2, 4]
    elif num == '*':
        coor = [1, 4]
    elif num == '#':
        coor = [3, 4]
    else:
        ## coor[0]
        if num % 3 == 1:
            coor[0] = 1
        elif num % 3 == 0:
            coor[0] = 3
        else:
            coor[0] = 2
        ## coor[1]
        coor[1] = ((num - 1) // 3) + 1
    return coor

def length(coor_x,coor_y): ## 좌표간의 거리
    return abs(coor_x[0]-coor_y[0]) + abs(coor_x[1]-coor_y[1])

def solution(numbers, hand):
    answer = ''
    l = '*'; r = '#'
        
    for i in numbers:
        if i % 3 == 1: ## 1, 4, 7
            answer += 'L'
            l = i
        elif i % 3 == 0 and i // 3 > 0: ## 3, 6, 9
            answer += 'R'
            r = i
        else: ## 2, 5, 8, 0
            if length(coor(i), coor(r)) > length(coor(i), coor(l)):
                answer += 'L'
                l = i
            elif length(coor(i), coor(r)) < length(coor(i), coor(l)):
                answer += 'R'
                r = i
            else:
                if hand == 'right':
                    answer += 'R'
                    r = i
                else:
                    answer += 'L'
                    l = i
            
    return answer