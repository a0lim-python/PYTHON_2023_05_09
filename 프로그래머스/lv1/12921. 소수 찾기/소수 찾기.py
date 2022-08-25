# 에라토스테네스의 체: 이중 for문 & True/False
def solution(n):
    answer = 0
    nums = [True] * (n + 1)
    nums[0] = False; nums[1] = False ## 0은 해당되지 않음 / 1은 소수가 아님
    
    for i in range(2, n + 1):
        if nums[i] is True:
            for j in range(2, (n // i) + 1): ## 소수 자신은 제외
                nums[i * j] = False
    
    answer = nums.count(True)
    return answer

# 에라토스테네스의 체 활용: while, for 문 & remove -> timeerror

def solution(n):
    answer = 0
    nums = list(range(2, n + 1))
    
    while nums != []:
        answer += 1
        prime = nums[0] # all[0]: 남아있는 소수의 최소값
        
        for i in range(1, max(nums) // prime + 1): ## 소수 및 소수의 배수 삭제 / 배수의 개수를 모르므로 for 문을 사용해서 완전 탐색 진행
            if prime * i in nums:
                nums.remove(prime * i)
        
    return answer

# someone else's answer: 에라토스테네스의 체 & for문 & set(차집합)

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1): ## 차집합으로 제거하므로 소수 여부 판별 불필요
        if i in num:
            num-=set(range(2*i,n+1,i)) ## i: 소수 / i의 배수를 삭제(n+1이 되기 전까지) / set: 차집합을 사용하여 해당 값을 리스트에서 제거
    return len(num)
