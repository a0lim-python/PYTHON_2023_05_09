def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekday = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'] ## 일자 % 7 이 작은 순서대로
    
    date = 0
    for i in range(a - 1):
        date += days[i]
        
    date += b
    answer = weekday[date % 7]
    
    return answer