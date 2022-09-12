N = int(input())
l = []
for i in range(N):
    l.append(input())
l = list(set(l)) ## 중복 제거
l.sort(key = lambda x: (len(x), x))

for j in l:
    print(j)
