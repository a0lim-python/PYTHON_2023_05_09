def ranking(pos_nums):         
    if pos_nums ==6:return(1)
    elif pos_nums==5:return(2)
    elif pos_nums==4:return(3)
    elif pos_nums==3:return(4)
    elif pos_nums==2:return(5)
    else: return(6)
    
def solution(lottos, win_nums):
    right_nums = 0
    result = []
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            right_nums+=1
    # 0_nums = lottos.count(0) 
    
    result.append(ranking(right_nums+lottos.count(0)))
    result.append(ranking(right_nums))
    answer = result
    return answer