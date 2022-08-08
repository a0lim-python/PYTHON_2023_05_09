* 자료구조
    - 메모리 공간 기반의 연속 방식(contiguous)
    - 포인터 기반의 연결 방식(link)
        + 추상자료형(ADT: Abstract Data Type)의 대부분의 실제 구현

* C언어의 배열  
![image](https://user-images.githubusercontent.com/104348646/183409135-6dc961d1-1db3-4de8-9e8f-56989f1a82ba.png)

* 동적 배열
: 크기를 지정하지 않고 자동으로 리사이징하는 배열
    - 리스트
    - 더블링(doubling): 미리 작은 초기 값으로 배열을 생성하고, 데이터가 추가되면서 모두 채워지면, 늘리고 모두 복사
    - 그로스 팩터(growth factor): 재할당 비율
        + 파이썬: 초반에는 2배씩 늘림(전체적으로는 약 1.125배)
    - 시간 복잡도: O(1)
        + 최악의 경우, 배열 할당을 위한 복사 작업에서 O(n) (발생 낮음)

![image](https://user-images.githubusercontent.com/104348646/183408329-19f7fd17-1f65-4327-92ce-1118b3f74d6d.png)

## 7 두 수의 합
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.  
![image](https://user-images.githubusercontent.com/104348646/183406755-dbd77fb8-d325-44ab-babe-7dde72a4a95c.png)

### 1. 브루트 포스(Brute-Force)로 계산
* 5284 ms
    - O(n^2)
```
def twoSum(self, nums: list[int], target: int) -> list[int]: ## 무차별 대입방식: 모든 조합을 더해서 일일히 확인
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

### 2. in을 이용한 탐색
* 864 ms
    - O(n^2)
```
def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums): ## enumerate: 순서가 있는 자료형(리스트 등)을 입력으로 받아 요소 값을 value, 인덱스를 key로 리턴
        complement = target - n ## target - n(첫번째 값)이 존재하는 지 확인

        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)] ## nums[i+1:].index(complement) + (i+1): i+1에서 시작하여 complement에 해당하는 index와 합함
```

### 3. 첫 번째 수를 뺀 결과 키 조회
* 48 ms
    - O(n) (평균적으로 O(1))
```
def twoSum(self, nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 키 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[nums] = i ## 요소 값이 key, index가 value

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]: ## 조건 성립 and 자기 자신을 더한 경우 제외
            return [i, nums_map[target - num]] ## index를 리턴
```

### 4. 조회 구조 개선
* 44 ms
    - O(n) (평균적으로 O(1))
```
    -- 3. '첫 번째 수를 뺀 결과 키 조회'를 간결하게 업그레이드
def twoSum(self, nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i] ## index를 리턴
        nums_map[num] = i ## 키 값을 바꿔서 딕셔너리로 저장: 계산 후 한 값 씩 저장하므로 자기자신을 더한 경우가 없음
```

### 5. 투 포인터 이용
* Error
    - O(n)
```
def twoSum(self, nums: list[int], target: int) -> list[int]:
    lerft, right = 0, len(nums) -1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left,right]
```
```
    -- cf) nums 정렬
nums.sort() ## -> 기존의 인덱스 찾기 불가 -> 해당 방법을 사용할 수 없음
```

### 고(Go) 구현
* 8 ms
```
// 고(Go): 풀이 #3과 동일하게 작성
=> 비슷한 코드여도 언어에 따라 성능 개선이 가능
```

## 8 빗물 트래핑
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.  
![image](https://user-images.githubusercontent.com/104348646/183408783-43eba115-c650-46d0-91c7-e8e67841774b.png)

### 1. 투 포인터를 최대로 이동
* 52 ms
    - O(n)
```
def trap(self, height: list[int]) -> int:
    if not height: ## 계산 불가인 경우 처리
        return 0

    volume = 0
    left, right = 0, len(height) - 1 ## 양 끝에서 시작
    left_max, right_max = height[left], height[right] ## 양 끝의 높이

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max) ## 이동하면서 가장 높은 height를 저장
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume
```
![image](https://user-images.githubusercontent.com/104348646/183408414-b59ed4e5-040a-46be-b3f6-a8fefdaa62f6.png)

### 2. 스택 쌓기
: 변곡점을 기준으로 격차만큼 물의 높이를 채움
* 56 ms
    - O(n) 가능(기본적으로 이전 항목을 한 번만 살펴봄)
```
def trap(self, height: list[int]) -> int:
    stack = [] ## LIFO(후입선출) / 이전의 인덱스들을 저장
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]: ## (현재 높이 > 이전 높이) 인 경우에 계속 반복하여 실행
            # 스택에서 꺼낸다
            top = stack.pop ## 

            if not len(stack):
                break
            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume
```

![image](https://user-images.githubusercontent.com/104348646/183408470-96795248-4018-4f0a-b484-0da88990d6b0.png)

## 9 세 수의 합
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라  
![image](https://user-images.githubusercontent.com/104348646/183406892-116546c1-47f1-4757-ab3a-7dbf7b12d785.png)

### 1. 브루트 포스로 계산
* TimeOut
    - O(n logn)
```
def threeSum(self, nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums) - 1):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
    return results
```

### 2. 투 포인터로 합 계산
* 884 ms
    - O(n^2)
```
def threeSum(self, nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort() ## 순서대로 정렬

    for i in range(len(nums) -2): ## len(nums) -2: 세 수의 합
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0: ## 합이 0보다 작으면 left 숫자를 크게
                left += 1
            elif sum > 0: ## 합이 0보다 크면 right 숫자를 작게
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])
    
                while left < right and nums[left] == nums[left + 1]: ## left, right와 같은 값이 있는 경우를 스킵
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1 ## 다음 경우를 계속해서 진행
                right -= 1

    return results
```
* 투 포인터
: 시작점과 끝점을 기준으로 하는 문제 풀이 전략
    - 일반적으로 배열이 정렬되어 있을 때 더 유용
    - cf) 슬라이딩 윈도우

## 10 배열 파티션 1
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.  
![image](https://user-images.githubusercontent.com/104348646/183407066-7f60cea9-2c70-4551-8edd-6033e4bd6b8f.png)

### 1. 오름차순 풀이
* 332 ms
```
def arrayPairSum(self, nums: list[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산: [1,2], [3,4]
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum
```

### 2. 짝수 번째 값 계산
* 308 ms
```
    -- 정렬된 상태에서는 짝수 번째에 항상 작은 값이 위치
def arrayPairSum(self, nums: list[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if 1 % 2 == 0:
            sum += n
    return sum            
```

### 3. 파이썬다운 방식
* 284 ms
```
def arrayPairSum(self, nums: list[int]) -> int:
    return sum(sorted(nums)[::2]) ## 2칸씩 건너뜀 = 짝수 번째
```

## 11 자신을 제외한 배열의 곱
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.  
나눗셈을 하지 않고 O(n)에 풀이하라.  
![image](https://user-images.githubusercontent.com/104348646/183407167-8afba008-1cd8-460f-9f76-249c122f2e45.png)

### 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    - O(n)
```
def productExceptSelf(self, nums: list[int]) -> list[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p=1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, 0 - 1, -1): ## range(3, -1, -1) = [3, 2, 1, 0]
        out[i] = out[i] * p
        p = p * nums[i]
    return out
```

* cf) O(n^2): 조건에 위배
```
def mine(self, nums: list[int]) -> list[int]:
    out = []
    product = 1
    
    for i in range(len(nums)):
        prod_nums = nums ## 자신을 제외한 숫자들의 집합
        prod_nums.remove(nums[i])
        for j in range(prod_nums):
            product *= j
        out.append(product)
    return out
```

## 12 주식을 사고팔기 가장 좋은 시점
한 번의 거래로 낼 수 있는 최대 이익을 산출하라  
![image](https://user-images.githubusercontent.com/104348646/183407226-eccef6fd-5ed7-4287-97a3-c1aacf1bda96.png)

### 1. 브루트 포스로 계산
* TimeOut
    - O(n^2)
```
def maxProfit(self, prices: list[int]):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price
```

### 2. 저점과 현재 값과의 차이 계산
* 64 ms
    - O(n)
```
def maxProfit(self, prices: list[int]) -> int:
    profit = 0 ## 첫 최댓값 변수 -> 최솟값으로 ## -sys.maxsize -> 입력값이 []인 경우엔 그대로 출력되는 문제
    min_price = sys.maxsize ## 첫 최솟값 변수 -> 최댓값으로

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit
```

* 최댓값과 최솟값
```
    -- 시스템이 지정할 수 있는 가장 높은/낮은 값
mx = -sys.maxsize
mn = sys.maxsize

    -- 무한대 값 지정
ms = float('-inf')
mn = float('inf')

    -- 임의의 값 지정
mn = 9999
-> 더 큰 값이 들어와서 최솟값이 교체되지 않을 수 있음 -> 지양
```
