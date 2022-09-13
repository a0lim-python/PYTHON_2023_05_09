N = int(input())

l = list()
for i in range(N):
    l.append(list(input().split()))

l.sort(key = lambda x: int(x[0]))

for j in l:
    print(int(j[0]), j[1])