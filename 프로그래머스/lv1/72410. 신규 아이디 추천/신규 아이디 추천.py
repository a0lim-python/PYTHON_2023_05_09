# someone else's answer

import re

def solution(new_id):
    ## 1. 소문자로 변환
    rec = new_id.lower()
    ## rec = re.sub('[A-Z]', '[a-z]', new_id) // ...!@[a-z]a[a-z]#*..y.abcdefghijklm ## 대문자가 '[a-z]' 문자로 변환됨
    
    # 2. 다른 특수문자 제거
    rec = re.sub('[^a-z0-9\-\_\.]','',rec)
    ## ^: 뒤의 문자가 없음
    ## \: 없어도 가능
    
    # 3. ..를 . 으로 치환
    rec = re.sub('[.]+','.',rec) ## 1개 이상의 .을 .으로 변환
    
    # 4. 맨 앞에 있는 . / 맨 뒤에 있는 . 삭제
    rec = re.sub('^[.]|[.]$','',rec)
    ## ^[.]: 맨 앞의 문자가 .
    ## |: 또는(or)
    ## [.]$: 맨 뒤의 문자가 .
    
    # 5. 빈 문자열 -> a로
    rec = re.sub('^$','a',rec)
    ## ^$: 맨 앞과 맨 뒤 사이에 문자가 없음 = 빈 문자열
    
    # 6. 문자열의 길이를 15 까지
    rec = rec[0:15]
    rec = re.sub('[.]$','',rec) ## 맨 뒤에 있는 . 삭제
    
    # 7. 문자열의 길이가 2 이하인 경우, 길이가 3이 될 때 까지 마지막 문자를 반복 입력
    rec = rec if len(rec) > 2 else rec + rec[-1] * (3 - len(rec))
    ## rec if len(rec) > 2: 길이가 2 초과인 경우, rec
    ## rec + rec[-1] * (3 - len(rec): 길이가 2 이하인 경우, rec + 마지막 문자열을 부족한 길이만큼 입력

    return rec
