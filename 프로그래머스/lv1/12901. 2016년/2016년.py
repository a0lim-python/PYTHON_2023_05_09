# datetime

def solution(a, b):
    import datetime
    weekdays = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    d = '2016-' + str(a) + '-' + str(b) ## '2016-a-b' 형식 구현
    x = datetime.datetime.strptime(d, "%Y-%m-%d") ## 연, 월, 일에 맞는 datetime을 매칭
    answer = weekdays[x.weekday()] ## weekday(): 요일 출력 (weekdays와 같게)
    return answer

# list & for & %

def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekday = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'] ## 일자 % 7 이 작은 순서대로
    
    date = 0
    for i in range(a - 1): ## 직전 월까지
        date += days[i]
        
    date += b ## 해당 월의 일 수
    answer = weekday[date % 7]
    
    return answer
