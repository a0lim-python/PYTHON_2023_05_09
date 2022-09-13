import re

def solution(new_id):
    rec = new_id.lower() # 1. 대소문자
    rec = re.sub('[^a-z0-9\-\_\.]','',rec) # 2. 다른 특수문자 제거
    rec = re.sub('[.]+','.',rec) # 3. ..를 . 으로 치환
    rec = re.sub('^[.]|[.]$','',rec) # 4. 맨앞^에 있는 . // -> 지우기('')
    rec = re.sub('^$','a',rec) # 5. 빈 문자열 -> a로
    rec = rec[0:15] # 6. 15 까지
    rec = re.sub('[.]$','',rec) # 마지막 . 삭제
    if len(rec)<= 2: #7. 3까지
        while len(rec) < 3:
            rec+=rec[-1]

    return rec