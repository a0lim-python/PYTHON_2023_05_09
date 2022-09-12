N = int(input())

for i in range(N):
    score = 0
    quiz = input().split('X')
    for j in quiz:
        score += len(j) * (len(j) + 1) // 2
    print(score)