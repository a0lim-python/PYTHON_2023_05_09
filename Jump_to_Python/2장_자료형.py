# 숫자
from abc import abstractstaticmethod
import builtins
from types import BuiltinFunctionType
from typing import BinaryIO, is_typeddict


a = 2; b=3
print(a+b) # a-b a*b a/b
b//a # 나눗셈의 몫
b%a # 나눗셈의 나머지

# 문자
a='A098'; b='C842a'
a+b # -, *, / 는 불가능
a*2 # a를 두번 반복

len(a) # 길이
a[1] # n번째 문자 : 0부터 시작
a[-1] #뒤에서 n번째 문자 = a[-0]
print(a[0:3]+b[-1]) # a[0:3] -> 0 이상 3 미만
a[:] # a 전체

aa='hello happy word'
aa = aa[:-1]+'l'+aa[-1] ; print(aa) # 값 수정

## 문자열 포매팅
"I eat %d apples." %3  ## 특정 위치에 숫자 변경
"I eat %s apples." % "ten" ## 특정 위치에 문자 변경
"I eat %d apples every %sday."%(3,'mon') #동시에 변경
"I eat %d%% apples" % 10 # 바로 뒤에 %를 붙일떈 %%
"%10s" %3 # 10개의 스페이스 공백
"%-10s" %3 # 뒤에 10개의 스페이스 공백
"%0.3f" %3.141592 # 소수 절삭(셋쨰자리까지)

## format 함수
"I eat {0} apples.".format(3) # {0}에 숫자/문자 대입
"I eat {0} apples every {1}day.".format(3,'mon')# 동시에 변경: 숫자로 변수 표시
"I eat {0} apples every {week}day.".format(3,week='mon')

## 정렬 및 공백
"{0:<10}".format("hi")  # 왼쪽 정렬 / 오른쪽: "{0:>10} (hi 포함 10개 단위)
"{0:^10}".format("hi") # 가운데 정렬
"{0:*<5}".format("hi") # 공백채우기: *로 공백 채움
"{0:0.4f}".format(3.141592) # 소수점 넷쨰자리까지
"{0:10.4f}".format(3.141592) # 오른쪽 정렬+소수 절삭
"{{ and}}".format() # {}포함 사용 시 {{}}

## f 문자열 포매팅(파이썬 3.6버전 이상)
number=7; week='sun'
f'I eat {number} apples every {week}day.'
f'{"hi":<10}' # 왼쪽 정렬
f'{3.141592:10.4f}' # # 오른쪽 정렬+소수 절삭

## 기타 함수
"hobby".count('b') # hobby에서 b의 개수 세기
"hobby".find('b') # b의 위치 (중복시 처음으로 나온 위치로 나옴)
"hobby".index('b') # find와 같음
",".join('abcd') # abcd의 각 문자 사이에 , 삽입
"hi".upper() # 대문자로 변환; lower(): 소문자로 변환
"    hi     ".lstrip() # 왼쪽 공백 지우기; rstrip: 오른쪽; strip(): 양쪽
"I eat apples".replace('apples',"bananas") # 특정 문자열 바꾸기 (기존,교체)
"I eat apples".split() # 공백 기준으로 문자열 나누기; split("): " 기준으로 문자열 나누기


# 리스트[]: 숫자/문자 모음 -> 모든 자료형 포함 가능
a = []
b=[1,2,"three"]
c=[1,2,["three",4]]
c[0]

c[2][0] # 리스트 내부의 요소 산출
c[0:1] # 슬라이싱
b+c # 연속해서 나열(=문자열 문법)
b*3 # b를 3번 반복 나열
len(c) # 리스트 길이
b[0]+"x" #오류 -> b[0]는 1로 숫자형(문자형과 + 불가능)
str(b[0])+"x" # => 문자형으로 변형 후 + 연산

## 리스트 수정과 삭제
a = [1,2,3,4,5]
a[-1]="five"; a  # 수정
del a[0]; a # 삭제 / del[2:]

## 리스트 관련 함수들
a=[1,2,3]
a.append(4); a # 맨 마지막에 요소 추가/ a.append(5:10)
a=[5,4,3,1,2]
a.sort(); a # 정렬(1->5 올림차순)
a.reverse(); a # 리스트를 역순으로 뒤집기(: 순서 정렬 없이 현재의 리스트 뒤집기)
a.index(3) # 리스트에서 x가 있는 위치 반환
a.insert(0,"b"); a # insert(a,b): a 위치에 b 요소 삽입
a.remove(3) ;a #리스트에서 첫번째로 나오는 x를 삭제
a.pop() # 리스트의 맨 마지막 요소를 출력 & 삭제
a # a.pop(x): x번째 요소를 출력& 삭제
a.count(2) # a.count(x): 리스트 안에 있는 x의 개수
a.extend(["hi","hello"]); a # a.extend([b]): 리스트 a에 요소 b를 삽입 * 리스트만 가능 => a+[b]

# 튜플(): 튜플의 항목 값은 삭제/변경 불가 <-> 리스트
t1=()
t2=(1,) ## 요소가 1개일 시 , 붙여야 함
t3= 1,2,3
t4=(1,2,('three',))

t4[2] ## 인덱싱
t4[1:] ## 슬라이싱

t11=(1,2,'a','b'); t12=(3,4)
t11+t12 # 뒤에 이어서 출력
t12 * 3 # t12를 3번 반복
len(t11) # 튜플의 길이

# 딕셔너리{}: key:value의 쌍 여러개의 집합(ex. 표)
dic={'name':'john','birth':960816}
a={1:'a'}; a[2]='b'; a # key:value = 2:'b'
a[3]=(1,2,3); a # value에 리스트, 튜플 가능
del a[3]; a # key가 3인 요소 삭제
a[1] # key가 1인 요소 추출
aa={1:'a',1:'b'}; aa # key가 중복된 경우 마지막 경우만 저장
aa={[1,2]:3} # key에 리스트,튜플, 딕셔너리는 불가능
dic.keys() # dic 딕셔너리의 key 추출 -> 추출된 객체를 바로 append, pop, sort 등의 함수 적용 불가
dic.values() # value 추출
dic.items() # key, value 쌍 추출
dic.clear() # 딕셔너리 안의 key, value 모두 삭제
dic.get('name') # key로 value 호출 = a['name]
dic.get('name','a') # a인 key는 존재하지 않음 -> name의 value만 호출
'name' in dic # 특정 key가 딕셔너리에 있는지 여부: T/F

# 집합 자료형: 변수들의 집합 -> 중복X, 순서X (cf.리스트, 튜플)
s1=set([1,2,3]); L1=list(s1);L1 # 또는 tuple(s1)

s1=set([1,2,3,4,5,6]); s2=set([4,5,6,7,8,9])
s1 & s2 # 교집합
s1|s2 # 합집합 = s1.union(s2)
s1-s2; s2-s1 # 차집합 = si.difference(s2)

s1.add("a"); s1 # 값 추가
s1.update("b","c"); s1 # 여러개 값 추가
s1.remove(1); s1 # 특정 값 제거

# 불 자료형: T/F
a=True; b=False; type(a) # class: bool
1 == 1; 2<1 #불 자료형(T/F 값 나옴)
if []:
    print("참")
else:
    print("거짓") #문자열, 리스트, 튜플, 딕셔너리: 값이 없음() -> 거짓

a=[1,2,3,4]
while a:
    print(a.pop()) # 요소가 없으면 False -> 값 산출 중지
bool('')

# 변수: 자료형(=객체)의 값을 저장하는 공간 -> 변수 이름 = 변수에 저장할 값
a = [1,2,3]; id(a)
b=a; id(b) # 복사 = id(a) => a와 b가 가리키는 대상이 동일
a[1]=4;a;b # 대상 같음 -> a가 변하면 b도 변함

# 변수를 가져오면서 주소 다르게 설정
a=[1,2,3]; b=a[:]; a[1]="a"; a; b # [:] 이용
import copy
a=[1,2,3];b=copy.copy(a);b is a # copy 모듈 이용

# 변수를 만드는 다양한 방법
a,b = ("1","2"); (a,b) = "1","2" # 튜플 변수 생성
[a,b] = "1","2"; a,b=["1","2"]  # 리스트 변수 생성
a=b="1" # 여러개 변수에 같은 값 대입
a=3; b=5; a,b=b,a; a; b # a,b 값 바꾸기

# 2장 연습문제
## 1
score_dic= {"국어" : 80, "영어" : 75,"수학" : 55}
score = (80+75+55)/3; score

## 2
13 % 2
if 13 % 2==0:
    print("짝수")
else:
    print("홀수")

## 3
pin = "881120-1068234"
front = pin[:6]; front
back = pin[-7:]; back

## 4
pin[7]

## 5
a = "a:b:c:d"
a.format(":","#")

## 6
list1 = [1,3,5,4,2]
list1.sort(); list1
list1.reverse() ; list1

## 7
list2 = ['Life','is','too','short']
list2[0]+ ' '+ list2[1]+ ' '+list2[2]+' '+list2[3]

## 8
tuple1=(1,2,3); temp=(4,)
tuple1+temp

## 9
a = dict(); a
a[[1]] = 'python'
a[250]
a[0]  # 비어있기 때문에 자리로 입력 불가

## 10
a = {'A':90, 'B':80, 'C':70}
a['B']
a.pop() #????????????
[a.values()]
a
a['B']
list(a.values())

a.pop()



## 11
a=[1,1,1,2,2,3,3,3,4,4,5]
set(a)

## 12 : b도 같이 변경. 같은 id이기 때문


