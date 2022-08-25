# sum & map & list & str

def solution(x):
    if x % sum(list(map(int,list(str(x))))) == 0:
        answer = True
    else:
        answer = False
    return answer

# someone else's answer 1: list comprehension & sum & str

def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

## 1. list comprehension을 사용해서 바로 자릿수의 합을 구함
## 2. int(c)의 합을 구하기 위해 sum을 사용
## 3. return에서 비교연산자 사용 -> True / False 지정이 필요 없음
