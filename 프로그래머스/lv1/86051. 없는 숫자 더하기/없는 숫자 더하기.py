def solution(numbers):
    import string
    all = list(map(int, string.digits))
    for i in range(0,10):
        if i in numbers:
            all.remove(i)
    all = list(all)
    answer = sum(all)
    return answer

## someone else's answer
def solution(numbers):
    answer = 45 - sum(numbers)
    return answer
