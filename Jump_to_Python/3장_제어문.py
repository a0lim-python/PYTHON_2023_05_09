# if문
## or, and
money = 2000; card=True
if money >=3000 or card:
    print("택시")
else:
    print("걷기")

## in
pocket = ['paper','cellphone', 'money']
if 'money' in pocket:
    print("택시")
else:
    print("걷기")

## pass: if 일 때 행동x, else만 행동
if 'money' in pocket:
    pass
else:
    print("걷기")

## elif
if 'money' in pocket:
    print("택시")
elif card == True:
    print("택시")
else:
    print("걷기")

## 조건부 표현식
print("택시") if 'money' in pocket else print("걷기")

# while: 조건이 만족될 시에만 반복해서 문장 수행 / 조건 x -> stop
## ex: if(1번 출력하고 다음 코드 진행) / while(for과 유사)(n번 계속 출력 / while 안에 if, += 사용)
money = 0
while money < 5000:
    money = money+1000 # money+=1000
    #print("잔액이 &d원 입니다." % money)
    print("잔액이 %d원 입니다." % money)
    if money >= 5000:
        print("택시")
################## input 다시보기
## 선택지 입력
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    number = int(input()) ### 선택지 입력받음
    print(prompt)

## break : while에서 강제로 빠져나오기
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
############################# input 다시 보기
# if 중복문
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

## continue: 조건이 맞지 않을 때 while의 맨 처음으로 돌아가기(맞지 않는 조건에 countiue 사용)
a=0
while a<10:
    a+=1
    if a % 2 == 0: continue
    print(a) ## 짝수일 때는 넘어가고 홀수만 출력

## 무한 루프: ctrl+C로 나가기
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

# for
test_list = ['1', '2', '3']
for i in test_list:
    print(i)

## 튜플 변수 사용(first,last)
test_num = [(1,2),(3,4),(5,6)]
for (first, last) in test_num:
    print(first+last)

## for + if
marks = [90,25,67,45,80]
num = 0
for i in marks:
    num+=1
    if i>=60:
        print("%d번 학생은 합격입니다." % num)
    else:
        print("%d번 학생은 불합격입니다." % num)

## for + continue
num=0
for i in marks:
    num+=1
    if i <60:
        continue
    print("%d번 학생 합격 축하합니다." % num)

## for + range
add = 0
for i in range(1,11): # 1에서 10까지(1이상 11 미만)
    add+=i
print(add)

for num in range(len(marks)):
    if marks[num] < 60:
        continue
    else:
        print("%d번 학생 축하합니다 %d점으로 합격입니다." % (num, marks[num]))

## 구구단: for + range
for i in range(2,10): # 구구단 2~9
    for j in range(1,10): # 구구단 1~9 곱하기
        print(i*j, end= " ") # 곱셉+ 간격 조정
    print(' ') # j가 한 번 돌 때마다 엔터(줄바꿈)

## 리스트 내포: 
### 기존
a = [1,2,3,4]
result=[]
for num in a:
    result.append(num*3) # a 요소마다 x3 해서 리스트로 결과 산출
print(result)
### 리스트 내포 사용
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
### 리스트 내포 + if
a = [1,2,3,4]
result = [num*3 for num in a if num % 2 == 0] # 짝수인 경우만 리스트 내포
print(result)
### for 중복 리스트 내포 
result = [x*y for x in range(2,10)
             for y in range(1,10)]
print(result) # 힌 리스트 안에 결과값 모두 저장
