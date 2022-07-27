class class1(object):
    """description of class"""

 #programmers_신고 결과 받기 -> 성공 but 시간초과
#@@@@@@@@@@@@@@@@@ 2번째 시도 : 신고 내용을 순서대로 신고자 list, 받은 사람 list로 나눈 후 코드 시작. -> 집계 후 다시 for 돌리는 것 방지


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

report=list(sorted(set(report))) ## 중복 신고 제거 - sorted로 순서 섞임 방지
# ['apeach frodo', 'apeach muzi', 'frodo neo', 'muzi frodo', 'muzi neo']

reporter=[] # 신고 한 사람 id
reported=[] # 신고 받은 사람 id
reported_count=[] # 신고 받은 사람 count
for i in range(0,len(id_list)):
    reported_count.append(0)
final_reported=[] # 신고 횟수가 k 이상인 reported id list
mail_reporter=[]
for i in range(0,len(id_list)): # mail 받을 신고자
    mail_reporter.append(0)

for i in range(0,len(report)): # reporter / reported 분리
    temp = report[i].split(' ')
    reporter.append(temp[0])
    reported.append(temp[1])



for j in range(0,len(report)):
    if reporter[j]==reported[j]: # 본인 신고 제거
        re.sub('[a-z]','',reporter[j])
        re.sub('[a-z]','',reported[j])

for h in range(0,len(id_list)): # reported 횟수 집계
    reported_count[h]=reported.count(id_list[h])

for q in range(0,len(reported_count)): # 최종 정지당한 reported
    if reported_count[q]>=k:
        final_reported.append(id_list[q])

for u in range(0,len(reported)):
    for r in range(0,len(final_reported)):
        if reported[u]==final_reported[r]:
            #one = reported[u]  ## muzi
            #mail_reporter[id_list.index(one)]
            one = id_list.index(reporter[u])
            mail_reporter[one]+=1
