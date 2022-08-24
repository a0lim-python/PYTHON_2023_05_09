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
