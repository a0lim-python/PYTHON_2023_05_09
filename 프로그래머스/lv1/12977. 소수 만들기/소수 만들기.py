# is_prime 함수 생성 & collections.Counter() & 삼중 for loop

def is_prime(num, i = 2): ## 소수 여부 판별
    if num == 2:
        return True
    else:
        while num > i:
            if num % i != 0:
                i += 1
            else:
                return False
        return True

def solution(nums):
    import collections
    
    answer = 0
    sums = []
    
    for i in range(len(nums)): ## 세개의 수 i, j, k를 더함
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i < j and j < k: ## 중복 제거
                    sums.append(nums[i] + nums[j] + nums[k])
    
    sum = collections.Counter(sums) ## 원소별 개수 출력
    
    for i in sum.keys():
        if is_prime(i) == True:
            answer += sum[i] ## i의 개수만큼 더함

    return answer

# someone else's answer 1: 사중 for loop안에서 소수 판별, 소수의 개수 세기를 한번에 처리

def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                number = nums[i] + nums[j] + nums[k]
                if len([m for m in range(2, number) if number % m == 0]) == 0: ## 소수 판별
                    answer += 1 # 소수의 개수 더함

    return answer

# someone else's answer 2: combinations (하나의 리스트에서 모든 조합을 구함)

def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3): ## 세 개의 수를 이용한 조합을 구함
        cand = sum(a)
        for j in range(2, cand): ## 소수 판별
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
