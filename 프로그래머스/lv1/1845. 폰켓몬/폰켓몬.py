# 최대 조합의 수

def solution(nums):
    if len(set(nums)) < len(nums) // 2: ## 뽑는 수보다 종류가 더 적은 경우
        answer = len(set(nums))
    else:
        answer = len(nums) // 2 ## 뽑는 수만큼 조합이 완성
        
    return answer
