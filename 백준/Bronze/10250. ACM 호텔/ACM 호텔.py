import math 

cnt = int(input())

for i in range(cnt):
    H, W, N = map(int, input().split()) ## height, Width, # of guests
    xx = str(math.ceil(N/H)) ## round up(올림)
    xx = xx.zfill(2) ## 1 -> 01 / 10 -> 10
        
    yy = str(N%H)
    if yy == '0':
        yy = str(H) ## when N is on top floor(N%H=0) // H
    
    print(int(yy+xx))
