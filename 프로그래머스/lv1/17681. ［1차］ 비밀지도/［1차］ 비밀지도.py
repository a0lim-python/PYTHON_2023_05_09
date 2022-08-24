def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = str(bin(arr1[i])[2:]).zfill(n) ## 10진수를 n자리 2진수로 변환
        arr2[i] = str(bin(arr2[i])[2:]).zfill(n)
        
        answer.append('')
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0': # 벽이 아닌 경우
                answer[i] += ' '
            else:
                answer[i] += '#'
        
    return answer