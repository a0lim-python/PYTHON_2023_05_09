N = int(input())
test = list(map(int, input().split()))
M = max(test)

for i in range(N):
    test[i] = test[i] / M * 100

print(sum(test)/N)