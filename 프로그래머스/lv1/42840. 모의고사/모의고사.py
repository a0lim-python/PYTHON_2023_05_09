# dict & % & sort lambda

rule = dict()
rule[1] = [1, 2, 3, 4, 5]
rule[2] = [2, 1, 2, 3, 2, 4, 2, 5]
rule[3] = [3, 3, 1, 1, 2, 2, 4, 4]
ans = dict() ## 맞은 개수 입력

for i in rule.keys(): ## 1, 2, 3번 학생별
    sol = 0
    for j in range(len(answers)):
        if answers[j] == rule[i][j % len(rule[i])]:
            sol += 1
    if sol != 0:
        ans[i] = sol

answer = sorted(ans.items(), key = lambda x: (-x[1], x[0])) ## sort(max(정답), 사전순(1,2,3))
answer = list(map(int, dict(answer).keys()))

# someone else's answer: enumerate
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers): ## 문제 정답 -> q: index, a: value
        for i, v in enumerate(p): ## 학생들의 답안 -> i: index, v: value
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)] ## 학생들의 정답 수 -> i: index, v: value ## 학생 번호 출력
