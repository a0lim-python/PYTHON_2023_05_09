X = int(input()) ## total price
N = int(input()) ## count

total = 0
for i in range(N):
    a, b = map(int, input().split())
    total += a * b

if X == total:
    print('Yes')
else:
    print('No')