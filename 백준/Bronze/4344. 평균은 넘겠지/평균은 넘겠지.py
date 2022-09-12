C = int(input())

for i in range(C):
    score = list(map(int, input().split()))
    num = score[0]
    score = score[1:]
    avg = sum(score)// num
    
    count = 0
    for j in score:
        if j > avg:
            count += 1
    
    print("%0.3f%%" % (count/num * 100))
    