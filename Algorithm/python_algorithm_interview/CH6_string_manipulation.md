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

![image](https://user-images.githubusercontent.com/104348646/183291500-3613f294-0974-4917-8564-c761649fa6c3.png)

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

## 3 로그 파일 재정렬
로그를 재정렬하라. 기준은 다음과 같다.  
    1. 로그의 가장 앞 부분은 식별자다. (ex. let1, let2, dig1, ..)  
    2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.  
    3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.  
    4. 숫자 로그는 입력 순서대로 한다.  
![image](https://user-images.githubusercontent.com/104348646/183291538-10433b99-4f31-4cd7-aed4-91deb23ec400.png)

### 1. 람다와 + 연산자를 이용
* 람다 표현식
  : 식별자 없이 실행 가능한 함수
```
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit(): ## 식별자를 제외한 문자열의 문자/숫자 여부 판별
            digits.append(log) ## 숫자들 모음
        else:
            letters.append(log) ## 문자들 모음

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key = lambda x: (x.split()[1:], x.split()[0])) ## sort: 정렬 / x.split()[1:]: 식별자를 제외한 문자열을 키로 함 / x.split()[0]: 문자열이 같은 경우, 식별자를 기준으로 정렬
    return letters + digits ## 문자 먼저 + 이후 숫자
```

* sorted  VS sort + 람다
```
## sorted
s = ['2 A', '1 B', '4 C', '1 A']
sorted(s) = ['1 A', '1 B', '2 A', '4 C'] ## 첫 문자를 기준으로 정렬

def func(x):
    return x.split()[1], x.split()[0]
s.sort(key = func)
s // ['1 A', '2 A', '1 B', '4 C'] ## 두 번째 문자, 이후 첫 번째 문자를 기준으로 정렬 가능

## 람다: 별도의 함수 선언 없이 가능
s.sort(key = lambda x: (x.split()[1], x.split()[0]))
s // ['1 A', '2 A', '1 B', '4 C']
```

## 4 가장 흔한 단어
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.
![image](https://user-images.githubusercontent.com/104348646/183291559-c5b8bab0-f03b-4b46-a577-dc97003b6eca.png)

### 1. 리스트 컴프리헨션, Counter 객체 사용
```
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph] ## 단어 문자가 아닌 모든 문자를 공백으로 치환 / \w: 단어 문자 / ^: not
        .lower.split() ## 소문자로 변환하여 공백 기준 split
            if word not in banned] ## banned를 제외한 단어 목록

    counts = collections.Counter(words) ## 단어의 개수 연산
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0] ## 가장 흔한 단어를 추출 / counts.most_common(1) = [('ball', 2)]
```

## 5 그룹 애너그램(문자를 재배열하여 다른 단어로 바꾸는 것)
문자열 배열을 받아 애너그램 단위로 그룹핑하라.  
![image](https://user-images.githubusercontent.com/104348646/183291576-5da01b49-15b8-42ec-b918-3283b2a5d7f0.png)

### 1. 정렬하여 딕셔너리에 추가
```
def groupAnagrams(self, str: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list) ## 존재하지 않는 키를 삽입할 경우, KeyError 방지

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word) ## sorted(word): 단어 정렬 / ''.join: 합쳐서 이 값을 키로 하는 딕셔너리 구성
    return list(anagrams.values)
```

* 여러 가지 정렬 방법
: 팀소트(Timsort)
    - 파이썬에서 시작된 고성능 정렬 알고리즘
```
    -- 기본 sorted
a = [2, 5, 1, 9, 7]
sorted(a) // [1, 2, 45, 7, 9]

b = 'zbdaf'
sorted(b) // ['a', 'b', 'd', 'f', 'z'] ## 문자열 정렬(리스트로 변환됨)
'',join(sorted(b)) // 'abdfz' ## 리스트를 문자로 결합

    -- 제자리 정렬: 리스트 내부를 정렬
        cf) sort(): 리턴값 없음(None을 리턴함)

c = ['ccc', 'aaaa', 'd', 'bb']
sorted(c, key=len) ## 문자열 길이를 기준으로 정렬 // ['d', 'bb', 'ccc', 'aaaa']

    -- 함수를 이용해 키 정렬
a = ['cde', 'cfc', 'aba']

def fn(s):
    return s[0], s[-1]
print(sorted(a, key=fn)) // ['aba', 'cfc', 'cde] ## 첫번째 기준: 맨 앞의 요소 / 두 번째 기준: 맨 뒤의 요소

sorted(a, key = lambda s: (s[0], s[-1])) ## // ['aba', 'cfc', 'cde] ## 람다를 이용한 표현
```
![image](https://user-images.githubusercontent.com/104348646/183291602-33727ba1-6e15-4589-9307-cb6b42193606.png)

## 6 가장 긴 팰린드롬 부분 문자열
가장 긴 팰린드롬 부분 문자열을 출력하라.  
![image](https://user-images.githubusercontent.com/104348646/183291637-d0b7d009-0a48-4c09-8d3d-86adeac5847a.png)

### 1. 중앙을 중심으로 확장하는 풀이
가장 긴 팰린드롬 부분 문자열을 출력하라.  

![image](https://user-images.githubusercontent.com/104348646/183291388-e31201e1-3fcd-4cb2-b865-c0e37a508896.png)  
![image](https://user-images.githubusercontent.com/104348646/183291666-81b0c25e-5593-4a6b-b394-c007782c1f2c.png)

```
def longestPalindrome(self, s: str) -> str:
    # expand 함수: 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str: ## 숫자들로 투 포인터를 구성
        while left >= 0 and right < len(s) and s[left] == s[right]: ## 팰린드롬 판별
            left -= 1 ## 투 포인터 확장
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을 때 빠르게 리턴 -> 속도 향상
    if len(s) < 2 or s == s[::-1]: ## 글자 수가 1개 or 문자열 자체가 팰린드롬인 경우
        return s
    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, ## i-1번째 가장 긴 팰린드롬을 저장
                     expand(i, i+1), ## 2칸
                     expand(i, i+2), ## 3칸
                     key = len) ## 길이가 가장 긴 문자열을 리턴
    return result
```

* 유니코드와 UTF-8
    - ASCII
        + 1바이트에 모든 문자를 표현
        + 1비트는 체크섬(checksum)으로 제외, 7비트(128글자)로 문자 표현
        + 한글/한자 문자는 2개 이상의 특수 문자를 합쳐서 표현 -> 에러
    - (기존) 유니코드(Unicode)
        + 1바이트로 표현 가능한 영문자도 2바이트 이상의 공간 사용 -> 비효율  
    - UTF-8
        + 문자의 전체 바이트를 결정해 불필요한 공간을 없앰
