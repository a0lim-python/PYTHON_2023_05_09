## 문자열(str)
* 입력 받기
  - input()
  ```
  a = input()
  a = int(input())
  a, b = map(int, input().split())
  a = list(map(int, input().split()))
  ```
  
  - sys.stdin.readline(): 반복 입력이 많은 경우, 시간 단축  
    : input()과 결과 같음. 단, 개행문자(\n)이 같이 입력 받아짐
  ```
  import sys
  for i in range(1000000):
    a = int(sys.stdin.readline()) // 0 ## 숫자는 int() 등으로 개행문자를 제거 cf) sys.stdin.readline() = '0\n'
    
  ## 값을 저장
  data = [sys.stdin.readline().strip() for i in range(1000000)] ## strip(): 문자열의 앞과 끝의 공백 문자를 제거
  ```

* 문자열 좌우 정렬
```
* ljust, center, rjust
s = ‘abcd’
n = 7
s.ljust(n) ## 왼쪽 정렬 // 'abcd   '
s.center(n) ## 가운데 정렬 '  abcd '
s.rjust(n) ## 오른쪽 정렬 // '   abcd'
```

* 문자열을 하나씩 나누어 리스트로 정리하기
```
a = '12345'
list(a) // ['1', '2', '3', '4', '5']
```

* 문자열 정렬(뒤집기)
  - array, list, tuple도 가능
  - [::-1]
```
a = '734 893'
a[::-1] // '398 437'
a[2:0:-1] // '437' ## a[0:2]인 '734'을 역순으로 뒤집기
```

* 단어 변환
  - replace
```
a = 'abc'
a = a.replace('a', '*')
print(a) ## '*bc'
```

* 변수 내의 위치 찾기
  - find
  ```
  a = 'abcd'
  a.find('a') // 0
  a.find('z') // -1
  ```
  - index
  ```
  a.index('a') // 0
  a.index('z') // ERROR
  ```

* 단어 삭제
  - remove: 값으로 삭제
  ```
  a = [1, 2, 1, 2, 3]
  a.remove(2)
  a // [1, 1, 2, 3] ## 처음 나오는 2를 삭제
  a.remove(5) // ValueError ## 없는 값을 삭제하는 경우 Error
  ```
  - del: 인덱스로 삭제
  ```
  a = [1, 2, 1, 2, 3]
  del a[3]
  a // [1, 2, 1, 3] ## a[3]을 삭제
  del a[7] // IndexError ## 없는 위치의 값을 삭제하는 경우 Error
  ```

* import string
```
string.ascii_lowercase ## 소문자 // abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase ## 대문자 // ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters ## 대소문자 모두 // abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits ## 숫자 //0123456789
```

* 순열과 조합
```
import itertools
arr = ['A', 'B', 'C']

# 순열

itertools.permutations(arr, 2) ## arr 리스트 내에서 2개를 선택하여 나열하는 경우의 수
// 결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 조합

itertools.combinations(arr, 2) ## arr 리스트 내에서 2개를 선택하는 경우의 수
// [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

## 숫자형(int, float, ...)

* divmode
```
divmode(10, 3) ## 몫, 나머지 // (3, 1)
```

* 올림/반올림/내림
  - math.ceil(올림)
  ```
  import math
  
  math.ceil(31.415) // 32
  ```
  - round(반올림)
  ```
  round(31.415) // 32
  round(31.415, 2) // 31.42 ## 숫자를 소숫점 2째 자리까지 반올림
  round(31.415, -1) // 31.415 ## 숫자를 십 단위까지 반올림
  ```
  - math.floor, math.trunc(내림)
  ```
  import math
  
  math.floor(31.415) // 31
  math.floor(-31.415) // -32
  
  math.trunc(-31.415) // -31 ## 0을 향해 내림
  ```
* 정렬
  - 문자열도 가능(알파벳 순서)
  - sort: 원본을 변경
  ```
  ## 기본
  a = [1,5,3,4,2]
  a.sort() ## 오름차순 // [1,2,3,4,5]
  a.sort(reverse = True) ## 내림차순 // [5,4,3,2,1]
  
  ## sort + lambda
  b = [[1,2], [7,4], [7,1]]
  b.sort(key = lambda x: x[1]) ## 리스트 내에서 두번째 원소를 기준으로 오름차순 정렬 // [[7,1], [1,2], [7,4]]
  b.sort(key = lambda x: (-x[0], x[1])) ## 리스트 내에서 첫번째 원소를 기준으로 내림차순 -> 두번째 원소를 기준으로 오름차순 정렬 // [[7,1], [7,4], [1,2]]
  
  ### 숫자, 문자 혼합 + 문자열 원소를 내립차순으로 정렬하는 경우
  b = [[20, 'S'], [21, 'J'], [21, 'D']]
  b.sort(key = lambda x: (x[0], -x[1])) // TypeError: bad operand type for unary -: 'str'
  b.sort(key = lambda x: (-int(x[0]), x[1], reverse = True)) ## 숫자형 원소에 int() 변환 + 오름차순/내림차순 반대로 + reverse = True
  ```
  
  - sorted: 원본은 유지, 새 리스트 생성
  ```
  a = [1,5,3,4,2]
  b = sorted(a) // [1,2,3,4,5]
  a // [1,5,3,4,2]
  ```
* 숫자(문자열) 앞에 0 채우기
  - zfill
```
a = '1'
a.zfill(2) // '01'
```

* % 표현으로 변환
```
* 0.f%%: 소수점 없이 정수처럼 표시
print( "%0.f%%" % 40) // 40%

* 0.2f%%, 0.3f%% 등, 사용하고 싶은 소수점 자리까지 표시
print( "%0.2f%%" % 40) // 40.00%
```

* 진법
  - n진법 -> 10진법
  ```
  * int(num, base = n) ## n진법으로 적힌 문자열 num을 10진법으로 변환
  ```
  - 10진법 -> 2, 8, 16진법
  ```
  print(bin(10)) ## 숫자 10을 2진수로 변환 // 'Ob1010'
  print(oct(10)) ## 숫자 10을 8진수로 변환 // 'Oo12'
  print(hex(10)) ## 숫자 10을 16진수로 변환 // 'Oxa'
  
  print(bin(10)[2:] ## 진법 표시 제거 // '1010'
  ```
  - 10진법 -> n진법(n != 2, 8, 16)
    ```
    ## 1
    import string

    tmp = string.digits + string.ascii_lowercase ## 소문자 포함 -> 16진법 이상도 가능
    def convert(num, base) :
        q, r = divmod(num, base) ## q: 몫, r: 나머지
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base) + tmp[r]

    print(convert(10,3)) ## 10을 3진법으로 변환 // '101'

    ## 2
    def solution(num):
        tmp = ''
        while num:
            tmp += str(n % n)
            num = num // n
        return tmp[::-1]
    ```
  - n진법 -> m진법: n진법 -> 10진법 -> m진법
    ```
    ## 위의 함수와 동일
    print(convert(int('4', base = 5), 3)) ## 5진법으로 표현된 '4'를 10진수로 변환 & 10진수를 3진법으로 변환
    ```

* 최대 공약수, 최소공배수
  - 유클리드 호제법
    ```
    def gcd(a, b): ## a, b의 최대공약수
        while b > 0:
            a, b = b, a % b
        return a

    def lcm(a, b): ## a, b의 최소공배수
        return a * b / gcd(a, b)
    ```

----------------------
## 리스트(list)

* 리스트 뒤집기
   - reverse()
```
a = '734 893'
a = list(a) // ['7', '3', '4', ' ', '8', '9', '3'] // 변수 지정 필요
a.reverse // ['3', '9', '8', ' ', '4', '3', '7'] ## 변수 변환 필요 없음
result = '.'join(a) // '398 437'
```

* 리스트를 공백으로 구분해 출력
  - 문자
  ```
  a = ['1', '2', '3', '4']
  ' '.join(a) // 1 2 3 4 ## ''안에 구분자 입력
  ```
  - 숫자
  ```
  1. 문자형으로 변환 후 출력 -> 공백 출력은 문자/숫자 구분이 없음
  2. end = ' '
  a = [1, 2, 3, 4]
  for i in a:
      print(i, end = ' ') ## ''안에 구분자 입력
  print()
  ```

* 두 리스트에서 같은 위치의 원소간의 집합/연산
  - zip
```
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist))) // [[1,4,7],[2,5,8],[3,6,9]]
```
```
## 여러 개의 Iterable 동시에 순회할 때 사용

list1 = [1,2,3,4]
list2 = [100,120,30,300]
list3 = [392,2,33,1]
answer = []

for num1, num2, num3 in zip(list1, list2, list3):
    print(num1+num2+num3)
// 493
// 124
// 66
// 305
```
```
## key 리스트와 value 리스트로 딕셔너리 생성하기

animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) // {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```
```
## i번째 원소와 i+1번째 원소의 차를 출력하기

def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]): ## mylist의 2번째 원소부터 시작하는 리스트를 이용하여 차를 구함
        answer.append(abs(number1 - number2)) ## abs: 절댓값으로 변환
    return answer

if __name__ == '__main__': ## 메인 함수(solution)의 선언, 시작
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))
```

## 튜플(tuple)

* tuple 형태의 반복구문
  - enumerate: (index, value)
```
t = [1,5,7,33,39,52]
for i in enumerate(t):
  print(i)
  
//
{0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
```

## 이중 리스트(double list)
```
## 이중 리스트 내에서의 zip(unzip)

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
list(zip(*board)) // [(0, 0, 0, 4, 3), (0, 0, 2, 2, 5), (0, 1, 5, 4, 1), (0, 0, 0, 4, 3), (0, 3, 1, 2, 1)]
list(map(list,(zip(*board)))) ## 리스트 내부의 tuple을 list형식으로 변환 // [[0, 0, 0, 4, 3], [0, 0, 2, 2, 5], [0, 1, 5, 4, 1], [0, 0, 0, 4, 3], [0, 3, 1, 2, 1]]
```

* 연결 리스트 구현
  - 노드 구현: 각 노드는 value(val)와 다음 노드의 값(next)를 가짐 -> 위치 정보
```
class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next
```
  - 연결 리스트 구현
```
  -- 재귀함수(my_function) 생성: solution 클래스에 저장
class solution:
  def my_function(self, l1: ListNode, l2: ListNode) -> ListNode: ## ListNode: 위의 ListNode 클래스를 사용(연결 리스트의 노드에 해당)
  rev = None
    if l1.val > l2.val:
      rev.append(l1.val)
    else:
      rev.append(l2.val)
    return

  -- l1 연결 리스트 생성
list1 = ListNode(1) ## val = 1
list2 = ListNode(2) ## val = 2
list3 = ListNode(4) ## val = 4
l1 = list1 ## l1 연결 리스트의 초기 값: list1 -> 1
list1.next = list2 ## 1의 다음 값은 list2(-> 2) => 1->2
list2.next = list3 ## 2의 다음 값은 list3(-> 4) => 1->2->4

  -- l2 연결 리스트 생성
list4 = ListNode(1) ## val = 1
list5 = ListNode(3) ## val = 3
list6 = ListNode(4) ## val = 4
l2 = list4 ## l1 연결 리스트의 초기 값: list4 -> 1
list4.next = list5 ## 1의 다음 값은 list5(-> 3) => 1->3
list5.next = list6 ## 5의 다음 값은 list6(-> 5) => 1->3->5

  -- 구현
head = my_function(l1, l2) ## my_function 실행
while head: ## 연결 리스트의 처음부터 마지막까지 반복
  print(head.val, end="") ## 첫번째 val을 출력
  if head.next:
    print("->", end="") ## 이후 "->"를 출력
  head = head.next ## head를 다음 값으로 지정
//
1->3->4
```
