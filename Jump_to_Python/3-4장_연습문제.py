## jump_to_python ## 3,4장 연습문제

## 3-1 - "shirt"

## 3-2
sum=0; i=0
while i<=1000/3:
    sum+= 3*i
    i+=1
print(sum) ## // 166833

## 3-3
i=1
while i<=5:
    print(i*'*')
    i+=1
    
## 3-4.
i=1
for i in range(1,101):
    print(i)
    i+=1   
    
## 3-5.
score=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
for i in range(0,len(score)):
    sum+=score[i]
print(sum/len(score))

## 3-6.
numbers = [1, 2, 3, 4, 5]
result = []
result=[n*2 for n in numbers if n % 2 ==1]
print(result)

## 4-1.
def is_odd(n):
    if n % 2 ==0:
        print("짝수")
    else:
        print("홀수")
        
## 4-2.
### 입력 개수를 모를 때 사용하는 가변인자
### *args: 정해지지 않은 수의 파라미터들 / **kwargs: 정해지지 않은 수의 키워드 파라미터들
def avg_nums(*args):  ## *args: 튜플 형태
    sum=0
    #i=2
    for i in args:
        sum+=i
    print(sum/len(args))
avg_nums(1,2,3)        

### 추가 예제
def number_and_name(*args,**kwargs): ## args: 튜플 형태 / kwargs: 딕셔너리 형태
    print(args,kwargs)
number_and_name(1,2,3,name="jay")

## 4-3.
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

## 4-4.
print("you","need","python") ## 공백이 삽입됨

## 4-5.
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() # 파일이 닫히지 않은 상황 -> f1.close()가 필요

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

### with 구문: close가 필요 없음
with oepn("test.txt",'w') as f1:
    f1.write("Life is too short!")
with open("test.txt",'r') as f2:
    print(f2.read)

## 4-6.
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt','a')  # 'a': 내용 마지막에 추가
f.write(user_input)
f.write("\n") # 엔터(줄바꿈)
f.close

## 4-7.
f = open('test.txt','r')
body = f.read()
f.close() ## 읽은 후 닫기

body = body.replace('java','python')

f=open('test.txt', 'w')
f.write(body)
f.close()

