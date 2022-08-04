import math 

cnt = int(input())

for i in range(cnt):
    H, W, N = map(int, input().split())
    xx = str(math.ceil(N/H))
    xx = xx.zfill(2)
        
    yy = str(N%H)
    if yy == '0':
        yy = str(H)
    
    print(int(yy+xx))