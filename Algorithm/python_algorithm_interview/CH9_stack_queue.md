# 스택(stack)
* LIFO(후입선출)
* push()  
: 요소를 컬렉션에 추가
* pop()  
: 아직 제거하지 않은 가장 최근에 삽입된 요소를 제거  
* 활용  
    - 컴퓨터 프로그램의 서브루틴에 대한 정보를 저장하는 자료구조
    - 아키텍처 레벨의 하드웨어 스택(메모리를 LIFO 형태로 할당/접근)
    - 거의 모든 애플리케이션
* 스택 버퍼 오버플로(stack buffer overflow)  
: 꽉 찬 스택에 요소를 삽입하여, 요소가 넘쳐서 발생하는 에러  
* 스택 추상 자료형(ADT: abstract data type)  

![image](https://user-images.githubusercontent.com/104348646/184862463-617a76df-7cf5-4a81-8be0-b2d18dc65d44.png)

** 연결 리스트를 이용한 스택 ADT 구현 **

## 20 유효한 괄호
괄호로 된 입력값이 올바른지 판별하라  
![image](https://user-images.githubusercontent.com/104348646/184862672-af5af027-5e5b-4399-be6b-c5320f17d6e9.png)

### 1. 스택 일치 여부 판별
* (, [, { : 스택에 push
* },  ], ) : 스택에 pop
* 결과와 매핑 테이블 결과가 매칭하는지 확인
```
def isValid(self, s: str) -> bool:
    stack = [] ## 리스트에서 push, pop 모두 O(1)로 동작
    table = {
        ')':'(',
        ']':'[',
        '{':'}', 
    }
    
    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in s: ## ex. s = ()[] -> char = (, ), [, ]
        if char not in table: ## '(, [, {' : 쌓음
            stack.append(char) ## push
        elif not stack or table[char] != stack.pop(): ## not stack: 예외 처리 ## '), ], }' 입력 -> table[char]: key와 맞는 value / stack.pop(): push 값
            return False
    return len(stack) == 0 ## 스택이 비어 있는지 여부 확인
```

## 21 중복 문자 제거
중복된 문자를 제외하고 사전식 순서(lexicographical order)로 나열하라.  
![image](https://user-images.githubusercontent.com/104348646/184862985-a005428a-08f7-4088-aeee-246456b5d434.png)

### 1. 재귀를 이용한 분리
* 52 ms
```
def removeDuplicateLetters(self, s: str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)): ## 중복 제거 & 정렬
        suffix = s[s.index(char):] ## 각 문자의 index들의 집합
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):# 해당 문자부터 시작했을 때, 기존의 모든 요소들을 포함하고 있을 경우
            return char + self.removeDuplicateLetters(suffix.replace(char, '')) ## char: 해당 문자 / 재귀: 해당 문자를 제거하여 반복
    return ''
```
![image](https://user-images.githubusercontent.com/104348646/184863045-d5086e7b-c2df-4113-a757-e3211181e969.png)  
  
![image](https://user-images.githubusercontent.com/104348646/184863177-9f881cfd-b4cf-40ea-b77c-fab2808ae110.png)  

### 2. 스택을 이용한 문자 제거
* 32 ms
```
import collections

def removeDuplicateLetters(self, s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), [] ## counter: key가 문자이고, value가 문자의 개수인 딕셔너리
    
    for char in s:
        counter[char] -= 1
        if char in seen: ## 중복 방지
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0: ## char < stack[-1]: 사전식 순서 / counter[stack[-1]] <= 0: 더이상 중복이 없음
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
        
    return ''.join(stack)
```
![image](https://user-images.githubusercontent.com/104348646/184863251-21227f0d-ec74-4abb-9971-3ced2a52f85c.png)  

![image](https://user-images.githubusercontent.com/104348646/184863323-0ae276fe-01bf-4b85-b54d-c4d293f1d0b5.png)  

## 22 일일 온도
매일의 화씨 온도(F) 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.  
![image](https://user-images.githubusercontent.com/104348646/184863455-687d0b27-ad69-4ea6-ac01-cc979eca2038.png)  

### 1. 스택 값 비교
```
def dailyTemperatures(self, T: List[int]) -> List[int]:
    answer = [0] * len(T) ## base
    stack = []
    for i, cur in enumerate(T): ## index, value
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > T[stack[-1]]: ## (현재 온도 > 스택에 쌓인 온도)인 경우
            last = stack.pop() ## 기준이 되는 날보다 날씨가 더 따뜻한 시점의 index
            answer[last] = i - last ## 기간 값을 저장
        stack.append(i) ## index 저장
        
    return answer
```

![image](https://user-images.githubusercontent.com/104348646/184863418-a2f7eaa3-6f65-48ba-a609-36bb652b52b4.png)  

# 큐(queue)  
: 시퀀스의 한쪽 끝에는 엔티티를 추가하고, 다른 반대쪽 끝에는 제거할 수 있는 엔티티 컬렉션
* FIFO(선입선출)
* 데크(deque) 자료형 사용 시 성능이 높아짐
* 활용  
    - 데크, 우선순위 큐 등의 변형
    - 너비 우선 탐색(BFS: Breadth-First Search)
    - 캐시 구현
* 파이썬의 큐: 적합하지 않음 -> 데크 사용: 양방향 삽입, 삭제 모두 O(1)

## 23 큐를 이용한 스택 구현
큐를 이용해 다음 연산을 지원하는 스택을 구현하라.  
1. push(x): 요소를 스택에 삽입한다  
2. pop(x): 스택의 첫 번째 요소를 삭제한다  
3. top(x): 스택의 첫 번째 요소를 가져온다  
4. empty(x): 스택이 비어 있는지 여부를 리턴한다  
![image](https://user-images.githubusercontent.com/104348646/184863587-4abfeb26-d2c3-4406-828a-fed55088c568.png)  

### 1. push()를 할 때 큐를 이용해 재정렬
* O(n)
  - FIFO에 해당하는 연산만 사용해서 구현
```
import collections

class Mystack:
    def __init__(self):
        self.q = collections.deque() ## deque 생성
        
    def push(self, x):
        self.q.append(x) ## 요소 삽입
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft()) ## 맨 왼쪽 값을 삭제하고 맨 뒤에 삽입
            
    def pop(self):
        return self.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0
```

## 24 스택을 이용한 큐 구현
스택를 이용해 다음 연산을 지원하는 큐을 구현하라.  
1. push(x): 요소를 큐 마지막에 삽입한다  
2. pop(x): 큐 처음에 있는 요소를 삭제한다  
3. peek(x): 큐 처음에 있는 요소를 조회온다  
4. empty(x): 큐이 비어 있는지 여부를 리턴한다  
![image](https://user-images.githubusercontent.com/104348646/185053193-43e2dc94-ef2c-4b0b-a23a-470efc943b2a.png)  

### 1. 스택 2개 사용
* O(1)
```
class MyQueue:
    def __init__(self): ## 큐와 달리 push 함수에서 맨 처음 요소를 뺄 수 없음 -> 2개의 스택 사용
        self.input = []
        self.output = []
        
    def push(self, x):
        self.input.append(x)
        
    def pop(self):
        self.peek() ## 기존과 반대 순서
        return self.output.pop() ## sel.output.pop(): 맨 뒤 요소 = sel.input.pop()의 맨 앞 요소
    
    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop()) ## self.input.pop(): 맨 뒤 요소를 제거 후 self.output에 추가: self.out은 self.input의 반대 순서로 저장
        return self.output[-1]
    
    def empty(self):
        return self.input == [] and self.output == []
```

## 25 원형 큐 디자인
원형 큐를 디자인하라  
![image](https://user-images.githubusercontent.com/104348646/185053403-9ff52eb7-4c9a-4673-958d-70c123ee2268.png)  
 
* 원형 큐(Circular Queue) (= 링 버퍼= Ring Buffer)  
: 마지막 위치가 시작 위치와 연결되는 원형 구조  
  - FIFO  
  - cf) 기존의 큐  
    : 공간이 다 차면 더이상 요소를 추가할 수 없음 <-> 앞쪽에 추가 가능  
  - enQueue: rear 포인터가 앞으로 이동(추가)  
  - deQueue: front 포인터가 앞으로 이동(삭제)  
  - rear 포인터와 front 포인터가 같은 위치에서 만나게 되면, 여유 공간이 없음 -> 공간 부족 에러 발생  

* 배열로 구현
![image](https://user-images.githubusercontent.com/104348646/185053678-0b362e13-d9f1-4c4f-b02a-c396935d2a70.png)  
![image](https://user-images.githubusercontent.com/104348646/185053718-74968cb1-8c1d-4ea0-9c8e-4316909696fb.png)  

```
class MyCircularQueue:
    def __int__(self, k: int):
        self.q = [None] * k ## base
        self.maxlen = k
        self.p1 = 0 ## front
        self.p2 = 0 ## rear
        
    # enQueue(): rear 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value ## rear 포인터에 값 입력
            self.p2 = (self.p2 + 1) % self.maxlen ## rear += 1 / 원형이므로 원형 큐의 길이인 k의 나머지값에 저장
            return True
        else: ## 종료 조건
            return False
        
    # deQueue(): front 포인터 이동 (추출 x)
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None ## 기존 front를 제거
            self.p1 = (self.p1 + 1) % self.maxien ## front += 1 / 원형이므로 원형 큐의 길이인 k의 나머지값에 저장
            return True
        
    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1] ## front 포인터의 위치
    
    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1] ## rear 포인터의 위치: rear에 값을 넣고 마지막에 위치를 +1 함 -> -1해야 value 확인 가능
    
    def isEmpty(self) -> bool:
        return self.pq == self.p2 and self.q[self.p1] is None
    
    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
```
