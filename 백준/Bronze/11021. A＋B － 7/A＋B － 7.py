T = int(input())

for i in range(1, T + 1):
    print('Case #' + str(i) + ': ' + str(sum(map(int, input().split()))))