## 리스트(list)
* 입력순서 유지
* 동적 배열로 구현됨
  
![image](https://user-images.githubusercontent.com/104348646/182998327-d32df219-a10f-4c1e-80b0-f7f8d823159d.png)

* 리스트 선언
```
a = list()
a = []
a = [1,2,3]
```

* 추가(append)
```
a.append(4) // [1,2,3,4]
```

* 인덱스를 지정해 요소 추가(insert)
```
a.insert(3,5) // [1,2,3,5,4]
```

* 다양한 자료형 삽입 가능
```
b = [1, 2, 3, 'python', True]
```

* 값 호출
```
a[3] // 5
```

* 슬라이싱(:)
```
a[1:3] // [2,3]
a[:3] // [1,2,3]
a[1:4:2] // [2,5] ## a[1:4]를 2칸 씩 건너 뛰어 호출함
```

* 존재하지 않는 인덱스를 조회하는 경우
```
a[9] // IndexError

    -- 에러의 예외 처리
try:
    print(a[9])
execpt IndexError:
    print('존재하지 않는 인덱스')
```

* 리스트의 요소 삭제
```
-- 인덱스로 삭제(del)
del a[1] // [1,3,5,4]

-- 값으로 삭제(remove)
a.remove(3) // [1,5,4]
```

* 리스트의 요소 추출(pop)
```
a.pop(2) // 4
print(a) // [1,5]
```

### 리스트의 특징

* 요소에 대한 포인터 목록을 가지고 있는 구조체로 선언됨
* 요소 추가/수정 시 포인터 목록의 사이즈를 조절
* 객체로 되어 있는 모든 자료형을 포인터로 연결하여 관리
* 정수, 문자, 불리언 등 제각기 다양한 타입을 동시에 관리 가능
* 단, 각 개체에 대한 참조로 구현하여 포인터의 위치, 타입 코드 확인 등의 절차가 필요함 -> 느린 속도  

![image](https://user-images.githubusercontent.com/104348646/182998246-dbe9429c-9234-4416-bba2-d47b438c0ace.png)

## 딕셔너리(dictionary)
: 키/값 구조로 이뤄짐
: 키/값 구조로 이뤄짐
* 해시 테이블로 구현됨
* 다양한 타입을 키로 사용 가능 <-> 리스트(인덱스: 숫자형)
* 입력/조회 모두 O(1)이 가능
* 파이썬 3.7부터 입력 순서 유지가 가능(3.6 이하의 버전: 유지 불가)

![image](https://user-images.githubusercontent.com/104348646/182998492-a0fddcc6-548a-42ad-896c-05594b058c58.png)

* 선언
```
a = dict()
a = {}
```

* 키 값 설정
```
a = {'key1':'value1', 'key2':'value2'}
a['key3'] = 'value3'
```

* 존재하지 않는 키를 조회하는 경우
```
a['key4'] // KeyError

    -- 에러의 예외 처리: 이후 삽입 등의 별도 추가 작업 가능
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

    -- 키 존재 여부 확인
if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키')
```

* key, value 값 호출
```
for k, v in a.items():
    print(k,v)

// key1 value 1
key2 value 2
...
```

* key 삭제
```
del a['key1'] // {'key2':'value2', 'key3':'value3'}
```

### 딕셔너리 모듈(collections)

* defaultdict
    - 존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하는 대신 디폴트 값으로 해당 키에 대한 딕셔너리 아이템을 생성
```
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
a // defaultdict(<class 'int'>, {'A':5, 'B':4})

    -- 존재하지 않는 키인 C를 생성(기존: KeyError)
a['C'] += 1 // defaultdict(<class 'int'>, {'A':5, 'B':4, 'C':1})
```

* Counter
    - 아이템에 대한 개수를 계산해 딕셔너리로 리턴
```
a = [1,2,3,4,5,5,5,6,6]
b = collections.Counter(a)
b // Counter({5:3, 6:2, 1:1, 2:1, 3:1, 4:1})

type(b) // <class 'collections.Counter'>

    -- 가장 빈도 수가 높은 요소 추출
b.most_common(2) // [(5,3), (6,2)]
```

* OrderdDict
    - 입력 순서 유지(버전 3.7: 자동 / 3.6 이하: 유지 설정필요)
```
collections.OrderDict({'banana':3, 'apple':4, 'pear':1, 'orange':2})
// OrderDict({'banana':3, 'apple':4, 'pear':1, 'orange':2}) 로 순서 유지
```

* 타입 선언 문법
```
a = [] ## list
a = () ## tuple
a = {} ## dict
a = {1} ## set
```
