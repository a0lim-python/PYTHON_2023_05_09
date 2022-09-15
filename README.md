## 문제 풀이 정리 양식
```
# [주요 사용 문법]

[문제 풀이 코드]

# someone else's answer 1: [주요 사용 문법]

[문제 풀이 코드]

## 1. [해당 문제 풀이 코드의 주요 포인트 1]
## 2. [해당 문제 풀이 코드의 주요 포인트 2]
...

# someone else's answer 2: [주요 사용 문법]

[문제 풀이 코드]

## 1. [해당 문제 풀이 코드의 주요 포인트 1]
...

...
```

* 예시
```
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
```

-----------------
## 차후 정리하면 좋을 자료들

* 연결리스트 개념 정립(특히 root)

* function annotation
  - https://bluese05.tistory.com/78

* 유니코드, UTF-8 인코딩
  - '파이썬 알고리즘 인터뷰' p162 ~ p165
