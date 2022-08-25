# 에라토스테네스의 체: 이중 for문 & True/False
def solution(n):
    ## 에라토스테네스의 체
    answer = 0
    nums = [True] * (n + 1)
    nums[0] = False; nums[1] = False ## 0은 해당되지 않음 / 1은 소수가 아님
    
    for i in range(2, n + 1):
        if nums[i] is True:
            for j in range(2, (n // i) + 1): ## 소수 자신은 제외
                nums[i * j] = False
    
    answer = nums.count(True)
    return answer
