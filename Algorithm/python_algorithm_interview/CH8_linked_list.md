* 연결 리스트(linked list)  
: 데이터 요소의 선형 집합으로, 데이터의 순서가 메모리에 물리적인 순서대로 저장되지는 않는다
    - 데이터를 구조체로 묶어서 포인터로 연결
    - 다양한 추상 자료형(ADT) 구현의 기반
    - 동적으로 삽입/삭제 간편
    - 연결 구조 -> 물리 메모리를 연속적으로 사용하지 않아도 됨 -> 관리 쉬움
    - 시간 복잡도
        + 탐색: O(n) <- 전체를 순서대로 읽어야 함
        + 시작/끝 지점에 삽입/삭제/추출: O(1)

![image](https://user-images.githubusercontent.com/104348646/183621062-8c8bebb9-f616-4ee7-b8a2-a2220eb54747.png)

* cf) 단일 연결 리스트 구현  
![image](https://user-images.githubusercontent.com/104348646/183621407-937d7054-1ae9-403a-82cd-972b43f8646c.png)  
![image](https://user-images.githubusercontent.com/104348646/183621488-975523a5-0f70-4c73-b4bc-07e28e9e44a8.png)

    - 노드 함수 생성
    ```
    class ListNode:
        def __init__(self, val = 0, next = None):
            self.val = val
            self.next = next
    ```

    - 노드 생성
    ```
    node1 = ListNode(1) ## val = 1
    node2 = ListNode(2) ## val = 2
    node3 = ListNode(4) ## val = 4
    ```

    - 연결 리스트에 새로운 노드 추가
    ```
    def append(self, ListNode):
        rev = self.head
        while rev.next:
            rev = rev.next
            rev.next = list1
    ```

    - 모든 노드 값 출력
    ```
    def print_all(self):
        rev = self.head
        while rev.next:
            print(rev.val)
            rev.next = rev
    ```

    - 특정 노드 값 출력
    ````
    `def get_node(self, index):
    `    count = 0
    `    node = self.head
    `    while count < index:
    `        count += 1
    `        node = node.next
    `    return node ## index 자리에 있는 node를 출력
    ````

    - 특정 인덱스에 노드 삽입
    ```
    def add_node(self, index, val):
        new_node = ListNode(val):
        if index == 0: ## 맨 앞에 삽입하는 경우
            new.node.next = self.head ## 새 노드와 self를 연결
            self.head = new_node ## self = 새 노드 + self
            return
        node = self.get_node(index-1) # 삽입할 자리의 직전 노드
        next_node = node.next ## next_node = 삽입할 자리의 직후 노드
        node.next = new_node ## 앞 연결: 삽입할 자리의 직전 노드 + 삽입 값
        new_node.next = next_node # 뒤 연결: 삽입 값 + 삽입할 자리의 직후 노드
    ```

    - 노드 삭제
    ```
    def delete_node(self, index):
        if index == 0:  ## 맨 앞을 삭제하는 경우
            self.head = self.head.next ## head를 두번째 값으로 이동
        node = self.get_node(index-1) ## 삭제할 자리의 직전 노드
        node.next = node.next.next ## 삭제할 자리의 직전 노드 + 삭제할 자리의 직후 노드
    ```


## 13 팰린드롬 연결 리스트
연결 리스트가 팰린드롬 구조인지 판별하라  
![image](https://user-images.githubusercontent.com/104348646/183622634-78ab4a7b-eee6-4239-9cb8-501b0e3ac8c2.png)

### 1. 리스트 변환
* 164 ms
    - O(n)
```
    -- 리스트의 pop(index)함수로 원하는 위치를 자유롭게 추출
def isPalindrome(self, head: ListNode) -> bool:
    q: list = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None: ## next가 존재하지 않을 때(마지막)까지
        q.append(node.val) ## node.val: 각 node의 data
        node = node.next ## 다음 node로 계속 진행

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != 1.pop() # 처음/마지막 값을 비교 후 리스트에서 삭제
            return False
    
    return True
```

### 2. 데크를 이용한 최적화
* 72 ms
  - O(1)
```
def isPalindrome(self, head: listnode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop() ## 처음 값: q.popleft() <-> cf) q.pop(0)
            return False

    return True
```

### 3. 고(Go)를 이용한 데크 구현
* 16 ms
```
    -- 데크 자료형 지원하지 않음
-> 데크 구조를 수기로 구현 -> 긴 코드 길이 + 비효율성
```

### 4. 런너를 이용한 우아한 풀이
* 64 ms
```
def isPalindrome(self, head: ListNode) -> bool:
    rev = None ## 느린 런너가 이동하면서 역순으로 연결 리스트 rev를 구성
    slow = fast = head ## 초깃값: head에서 시작
    # 런너를 이용해 역순 연결리스트 구성
    while fast and fast.next: ## next가 존재하지 않을 때(마지막)까지
        fast = fast.next.next ## 빠른 런너는 두칸 씩
        rev, rev.next, slow = slow, rev, slow.next ## rev: 느린 런너의 경로를 rev로 저장 / rev.next = rev: 기존 rev와 연결 (2 -> 1 -> None) / slow = slow.next: 느린 런너는 한칸 씩
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
```

![image](https://user-images.githubusercontent.com/104348646/183621854-55198ab9-bc7b-4616-bdb8-494294354904.png)

* 런너 기법(Runner)
: 한 포인터가 다른 포인터보다 앞서게 하여 연결리스트를 순회하는 투 포인터 기법
    - 병합 지점, 중간 위치, 길이 등을 판별하는 데 유용
    - 대개 빠른 런너는 2칸, 느린 런너는 1칸 씩 이동
    - 빠른 런너가 연결리스트의 끝에 도달 -> 느린 런너는 중간 지점에 위치 => 찾은 중간 위치를 다양하게 활용 가능

* 다중 할당(Multiple Assignment)
: 2개 이상의 값을 2개 이상의 변수에 동시에 할당하는 것
```
    -- ex) rev = 1, slow = 2->3인 경우
rev, rev.next, slow = slow, rev, slow.next ## 작업이 동시에 발생 // rev = 2->3 / rev.next = 1 / slow = 3

-> 두 줄로 분기
rev, rev.next = slow, rev ## rev = 2->3 / rev.next = 1 => (rev = slow: 동일 참조 됨) => rev = 2->1 
slow = slow.next ## -> slow = 2->1 / slow = 1
```

## 14 두 정렬 리스트의 병합
정렬되어 있는 두 연결 리스트를 합쳐라.  
![image](https://user-images.githubusercontent.com/104348646/183900804-50745f37-4dff-45a8-a0ae-83e1231c1c0f.png)

### 풀이 1. 재귀 구조로 연결
```
def mergeTwoLists(self, l1:ListNode, l2: ListNode) -> ListNode: ## l1/l2: 두 연결 리스트의 첫 번째 값
    if (not l1) or (l2 and (l1.val > l2.val)):
        l1, l2 = l2, l1 ## l1, l2 스왑
    if l1: 
        l1.next = self.mergeTwoLists(l1.next, 12) ## self.mergeTwoLists: 재귀호출
    return l1
```

![image](https://user-images.githubusercontent.com/104348646/183900905-09523033-ccc1-442d-974b-15d8649e1bb8.png)

* 연산자 우선순위  
![image](https://user-images.githubusercontent.com/104348646/183901011-5dd05bea-1ced-42ac-872e-b5e9b6c15131.png)

* 변수 스왑
```
    -- 임시변수 사용
temp = a
a = b
b =temp

x = 9; y = 4
x += y ## x = 9 + 4 = 13
y = x-y ## y = 13 - 4 = 9
x -=y ## x = 13 - 9 = 4

    -- 다중 할당(파이썬, C 가능)
a: int = 1
b: int = 2
a, b = b, a
```
## 15 역순 연결 리스트
연결 리스트를 뒤집어라.  
![image](https://user-images.githubusercontent.com/104348646/183901402-1401e862-a496-41cc-9378-988d7f406af4.png)

### 풀이 1. 재귀 구조로 뒤집기
* 40 ms
```
def reverseList(self, head: ListNode) -> ListNode:
    def reverse(node: Listnode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)
```

![image](https://user-images.githubusercontent.com/104348646/183901611-819fb842-6dea-4e19-9cb3-4d22f6843dae.png)

### 풀이 2. 반복 구조로 뒤집기
* 32 ms
```
def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None ## node: 현재 노드 / prev: result

    while node:
        next, node.next = node.next, prev ## next: node 다음에 추가할 노드
        prev, node = node, next

    return prev
```

![image](https://user-images.githubusercontent.com/104348646/183901661-6a3945ca-3a6e-41c0-ad5d-74a213665408.png)
