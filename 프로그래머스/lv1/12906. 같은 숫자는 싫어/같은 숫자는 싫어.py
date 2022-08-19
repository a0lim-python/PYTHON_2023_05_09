def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i] == answer[-1]: ## num is same with pre-num
                continue
            else:
                answer.append(arr[i])
    

    return answer