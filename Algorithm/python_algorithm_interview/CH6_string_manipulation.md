## 1 유효한 팰린드롬(앞뒤가 똑같은 단어나 문장)
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.  
ex) race a car

### 1. 리스트로 변환
* 304 ms
    - list pop: O(1)
```
def isPalindrome(self, s:str) -> bool: ## 변수: self / s: 문자형으로 지정 / -> bool: 값이 T/F bool 형태
    strs = []
    for char in s:
        if char.isalnum(): ## 영문자, 숫자 여부를 판별
            strs.append(char.lower()) ## char.lower(): 모두 소문자로 변환

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): ## 맨 앞의 값(strs.pop(0))과 맨 뒤의 값(strs.pop())을 하나씩 매칭
            return False

    return True
```

### 2. 데크 자료형을 이용한 최적화
* 64 ms
    - deque pop: O(n)
```
def isPalindrome(self, s:str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
    if strs.popleft() != strs.pop():
        return False

    return True
```

### 3. 슬라이싱
* 36 ms
```
def isPalindrome(self, s:str) -> bool:
    s = s.lower() ## 소문자로 변환

    # 정규식으로 불필요한 문자 필터링: 영문자, 숫자만 남음
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] ## 슬라이싱 [::-1]: 문자열 뒤집기
```

![image](https://user-images.githubusercontent.com/104348646/183067548-795918b5-3d4b-4b59-aea6-f17bb8d12eba.png)

### 4. C구현
* 4 ms
```
```

## 문자열 뒤집기
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
![image](https://user-images.githubusercontent.com/104348646/183071268-b3adda3e-1a35-4548-988b-1530c780d366.png)

### 1. 투 포인터를 이용한 스왑
* 216 ms
```
def reverseString(self, s: List[str]) -> None: ## List[str]: s를 리스트 안의 문자형으로 지정 / -> None: 출력값 없음
    left, rifht = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left] ## 왼쪽 문자와 오른쪽 문자를 스왑
        left += 1
        right -= 1
```

### 2. 파이썬다운 방식(reverse())
* 208 ms
```
def reverseString(self, s: List[str]) -> None:
    s. reverse()
```

### 3. 그 외(슬라이싱)
* 공간 복잡도가 O(1)인 경우 변수 할당 처리에 제약
```
def reverseString(self, s: List[str]) -> None:
    s = s[::1]

    -- 제약을 해결하는 코드
def reverseString(self, s: List[str]) -> None:
    s[:] = s[::-1]
```
