
# 함수
def add(a,b):
    return a+b
add(3,5)
## 매개변수, 인수 차이: 매개변수(def)-함수에서 입력하는 변수 / 인수(print): 함수 사용할 때의 입력값

## 입력값이 없는 함수
def say():
    return 'Hi'
print(say())

## 결과값이 없는 함수: 변수를 바꾸지 않음(return 사용 x) / print 출력만
def add(a,b):
    print("%d, %d의 합은 %d입니다" % (a,b,a+b))
add(3,4); print(a) ## a가 설정되지 않음

## 입력값, 결과값 모두 없는 함수: 변수 없음, return 없음, print 출력만
def say(): 
    print('Hi')
say()

## 매개변수 순서 바꿔서 설정하기
def add(a,b):
    return a+b
add(b=5, a=3)

## 입력값이 몇 개 일지 모를 때: 매개변수 앞에 * 붙이기
def add_many(*args):
    result = 0
    for i in args:
        result+=i
    return result
add_many(1,2,3,4,5,6,7,8,9,10)

## 하나의 매개변수 + 여러개의 매개변수 혼합
def add_mul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result+=i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result*i
    return result
add_mul("mul",1,2,3,4,5)

## 키워드 파라미터: 모두 딕셔너리로 출력 / 매개변수 앞에 **
def print_k(**k):
    print(k)
print_k(a=1);print_k(name='foo', age=3)

## return 여러개인 함수
def add_and_mul(a,b):
    return a+b, a*b
add_and_mul(3,4) ## 결과값 a+b와 a*b가 하나의 튜플로 출력
result1, result2 = add_and_mul(3,4); result1; result2 ## 결과값을 개별로 출력하기

## return 중복 : 불가능. 첫번째 return만 실행
def add_and_mul(a,b):
    return a+b
    return a*b
add_and_mul(2,3)

## return:if 조건에 따라 결과값 없이 빠져나오기
def say_nick(nick):
    if nick=="fool":
        return
    print("My name is %s" % nick)
say_nick("April"); say_nick("fool")

## 매개변수 초깃값 설정: 초깃값 설정하는 변수를 맨 마지막에 배치
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("Amy",20);say_myself("Amy", 20, False)

## 함수의 출력값 범위: 함수 내의 a 값이 함수 밖의 a에 적용되는 것은 아님
a = 1
def vartest(a):
    a = a+1
vartest(a); print(a) ## 2 != 1

### 함수 밖의 변수를 변경하는 방법
#### 1. return + a=def(a) 대입
a=1
def vartest(a):
    a+=1
    return a
a = vartest(a);print(a)

#### 2. global: 함수 안에서 함수 밖의 a 변수 사용(권장x: 함수의 독립성)
a=1
def vartest():
    global a
    a+=1
vartest();print(a)

#### lambda: (=def) 간결한 함수(return 없이 결과값 출력)(최소 2개 이상의 매개변수) or def 사용 불가 시
add = lambda a,b: a+b
result = add(3,4); print(result)

# input : 입력값을 모두 문자열로 취급
a= input() ## 대화형 창에서 입력 'Life is too short'
print(a) ##변수 a에 입력값 대입

## 프롬프트 사용
number = input("숫자를 입력하세요: ")

# print
print("Life" "is" "too short") ## + 연산과 동일(= print("Life"+"is"+"too short")), 문자열 붙여서 출력

print("life","is","too short") ## 문자열 띄어쓰기
for i in range(1,10):   ## end=' ' : 한줄에 결과값 출력(결과값 사이에 " "이 추가)/ "*" 등도 가능
    print(i, end=' ')

# 파일 관련 함수: r  =읽기/w = 쓰기/a = 마지막에 추가
f = open("C:\\Users\\ahyou\\Desktop\\new.txt", 'w') ## w(쓰기): 파일이 기존에 존재하는 경우,기존 삭제 & 새 파일 생성
f.close() ## 파일 닫기

## w(쓰기) : 파일에 출력값 적기
f = open("C:\\Users\\ahyou\\Desktop\\new.txt", 'w')
for i in range(1,10):
    data = "%d번째 줄입니다,\n" % i
    f.write(data)
f.close()

## r(읽기)
### readline
f = open("C:\\Users\\ahyou\\Desktop\\new.txt", 'r')
line = f.readline() ## 첫번째 줄만 출력
print(line)
f.close()

### 모두 출력 : while True 무한루프 사용
f = open("C:\\Users\\ahyou\\Desktop\\new.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

### 입력 파일을 모두 출력
### 안 됨(점프투파이썬)
while True:
    data = input()
    if not data: break
    print(data)

### 됨 : with open - 입력(C:\Users\ahyou\Desktop\new.txt)

with open(input(), 'r') as help:
    x = help.read()
    print(x)
    print(type(x))

###readlines: 모든 줄 읽기
f = open("C:\\Users\\ahyou\\Desktop\\new.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip() ## 추가 코드: 줄 끝의 줄바꿈 문자를 제거할 때
    print(line)
f.close()

### read: 파일의 전체 내용 
f = open("C:\\Users\\ahyou\\Desktop\\new.txt", 'r')
data = f.read()
print(data)
f.close()

## a(내용 추가)
f = open("C:\\Users\\ahyou\\Desktop\\new.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

## with open: f.close(파일 열기/닫기) 자동
with open("C:\\Users\\ahyou\\Desktop\\new.txt", 'w') as f:
    f.write("Happy")

## sys 모듈
import sys
args = sys.argv[1:]
for i in args:
    print(i)

import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ') ## 대문자로 불러오기

a = []
a.append(1)
