def solution(price, money, count):
    answer = price * sum(range(1, count + 1)) - money
    if answer < 0:
        answer = 0

    return answer