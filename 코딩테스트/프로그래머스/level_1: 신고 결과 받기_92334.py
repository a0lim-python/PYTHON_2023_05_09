def solution(id_list, report, k):
    report=list(sorted(set(report))) ## 중복 신고 제거 - sorted로 순서 섞임 방지

    reporter=[] # 신고 한 사람 id
    reported=[] # 신고 받은 사람 id
    reported_count = [0 for i in range(0,len(id_list))] # 신고 받은 사람 count
    final_reported=[] # 신고 횟수가 k 이상인 reported id list
    final_reporter=[] # 신고 횟수가 k 이상인 reporter id list (=mail 받을 신고자 id)

    reporter = [report[i].split(' ')[0] for i in range(0,len(report))]
    reported = [report[i].split(' ')[1] for i in range(0,len(report))]

    reported_count = [reported.count(id_list[h]) for h in range(0,len(id_list))] # reported 횟수 집계

    final_reported = [id_list[q] for q in range(0,len(reported_count)) if reported_count[q]>=k] # 최종 정지당한 reported

    final_reporter=[reporter[u] for u in range(0,len(reported)) if reported[u] in final_reported] # mail 받을 reporter id

    answer=[final_reporter.count(id_list[z]) for z in range(0,len(id_list))] # reporter 별 mail 받을 개수
    return answer
