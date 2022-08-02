### 몫과 나머지 출력하기
* divmod
	- 큰 숫자를 계산하는 경우에 a//b, a%b보다 속도가 빠름
```
a = 7
b = 5
print(*divmode(a,b)) // 1 2
```

### n진법으로 표기된 string을 10진법 숫자로 변환하기
* int(x, base = 10)
```
## 5진법으로 적인 문자열 ‘3212’를 10진법으로 바꾸기
num = ‘3212’
base = 5
answer = int(num, base)
print(answer) // 432
```

### 문자열 정렬
* ljust, center, rjust
```
s = ‘abcd’
n = 7
s.ljust(n) ## 왼쪽 정렬 // 'abcd   '
s.center(n) ## 가운데 정렬 '  abcd '
s.rjust(n) ## 오른쪽 정렬 // '   abcd'
```

### 모든 알파벳/숫자 출력하기
* string

```
import string

string.ascii_lowercase ## 소문자 // abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase ## 대문자 // ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters ## 대소문자 모두 // abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits ## 숫자 //0123456789
```

### 원본을 유지한 채, 정렬된 리스트 구하기
* sorted
```
list1 = [3,2,5,1]
list2 = sorted(list1) // [1,2,3,5]
````

### 2차원 리스트 뒤집기
* zip
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

### 모든 멤버의 type 변환하기
* map
```
list1 = ['1', '100', '33']
list2 = list(map(int, list1)) /// [1, 100, 33]
```
```
## 리스트의 각 원소의 길이를 담은 리스트를 출력

def solution(mylist):
	answer = list(map(len,mylist))
	return answer
// input: [[1, 2], [3, 4], [5]]
// output: [2, 2, 1]
```

### sequence 멤버를 하나로 이어붙이기
* join
```
my_list = ['1', '100', '33']
answer = ‘’.join(my_list) // ‘110033’
```

### 삼각형 별 찍기
* sequence type의 * 연산
```
n = int(input().strip())
for i in range(0,n+1):
    print('*'*i)
// input: 3
.. output:
*
**
***
```

### 곱집합(Cartesian product) 구하기
* product
```
import itertools

iter1 = ‘ABCD’
iter2 = ‘xy’
iter3 = ‘1234’

print(list(itertools.product(iter1, iter2, iter3)))
// [('A', 'x', '1'), ('A', 'x', '2'), ('A', 'x', '3'), ('A', 'x', '4'), ('A', 'y', '1'), ('A', 'y', '2'), …, ('D', 'y', '4')]
```

### 2차원 리스트를 1차원 리스트로 만들기
* from_iterable
```
my_list = [[1, 2], [3, 4], [5, 6]]
// output: [1, 2, 3, 4, 5, 6]

## 방법 1: sum

answer = sum(my_list,[])

## 방법 2: itertools.chain

import itertools
list(itertools.chain.from_iterable(my_list))

## 방법 3: itertools, unpacking

import itertools
list(itertools.chain(*my_list))

## 방법 4: list comprehension

[element for array in my_list for element in array]

## 방법 5: reduce 1

from functools import reduce
list(reduce(lambda x, y: x+y, mylist))

## 방법 6: reduce 2

from function import reduce
import operator
list(reduce(operator.add, my_list))

## 방법 7: numpy flatten

import numpy as np
np.array(my_list).flatten().tolist() ## 단, 원소의 길이가 동일한 경우에만 사용 가능: [[1,2],[3,4],[5]] (X)
```

### 순열과 조합(combinations, permutations)
* itertools.permutation
```
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) ## 3개의 원소로 수열 만들기 // ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
print(list(map(''.join, itertools.permutations(pool,2)))) ## 2개의 원소로 수열 만들기 // ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
```

### 가장 많이 등장하는 알파벳 찾기
* counter
```
import collections

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) ## 1의 개수 // 4
print(answer[3])  ## 3의 개수 // 3
print(answer[100]) ## 100의 개수 // 0
```

### List comprehension의 if문
* list comprehension 안의 조건문
```
## 정수를 담은 리스트 mylist를 입력받아, 이 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴


mylist = [3, 2, 6, 7]
even = [i**2 for i in mylist if i%2 == 0]
```

### 
```
import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)): ## math.sqrt: 제곱근
            print('found')
            break
    else:
        print('not found')
```

### flag 대신 for-else 사용하기
* for-else
	- if-else와 마찬가지로 for-else절을 사용
```
## 본 문제에서는 자연수 5개가 주어집니다. 숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고 모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는 코드를 작성해주세요.

import math

nums = [int(input()) for _ in range(5)] ## input을 5번 받음: 특정 변수를 이용하지 않는 단순 반복이므로 i 대신 _을 입력
multi = 1

for i in range(0,len(nums)):
    multi *= nums[i] 
    if math.sqrt(multi) == int(math.sqrt(multi)): ## if 제곱근이 int
        print('found')
        break
else:
    print('not found')
```

### 두 변수의 값 바꾸기 – swap
```
## a = 3, b = 'abc'를 a = 'abc', b = 3 으로 바꾸기

a = 3
b= ‘abc’
a, b = b,a
```

### 이진 탐색하기 – binary search
* bisect
```
## 일반 이진 탐색문: 오름차순 정렬된 배열에서 원하는 숫자를 찾음

def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3)) ## 3보다 작은 숫자의 개수

## bisect.bisect
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
```

### 클래스 인스턴스 출력하기 – class의 자동 string casting
* _ _ str _ _
```
## 2차원 평면 위의 점을 나타내는 Coord 클래스의 인스턴스를 (x 값, y 값)으로 출력하기

class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)
```

### 가장 큰 수, inf
* inf
```
## 최솟값을 저장하는 변수에 아주 큰 값을 할당하는 코드

min_val = float(‘inf’)
min_val > 10000000000 // True

## 최댓값을 저장하는 변수에 아주 작은 값을 할당하는 코드

max_val = float(‘-inf’)
```

### 파일 입출력 간단하게 하기
* with – as
	- with – as 블록이 종료되면 파일이 자동으로 close 됨(파일 close 코드가 필요 없음)
	- readlines가 EOF까지만 읽음(while 문 안에서 EOF를 체크할 필요 없음)
	- socket, http 등에서도 사용 가능
```
## myfile.txt라는 파일을 읽는 코드

with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
```
