# bin & zfill & for

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = str(bin(arr1[i])[2:]).zfill(n) ## 10진수를 n자리 2진수로 변환 -> 문자열로 변환
        arr2[i] = str(bin(arr2[i])[2:]).zfill(n)
        
        answer.append('')
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0': # 벽이 아닌 경우
                answer[i] += ' '
            else:
                answer[i] += '#'
        
    return answer

# someone else's answer: zip, bin, 비트연산자, rjust, replace

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:]) ## 1. i, j를 이진변환 -> 2. 같은 자리에 모두 0이 오면 0, 1이 있으면 1을 출력
        a12=a12.rjust(n,'0') ## zfill(n)과 같은 역할
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
