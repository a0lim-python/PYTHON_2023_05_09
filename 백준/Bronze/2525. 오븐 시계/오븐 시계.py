A, B = map(int,input().split()) ## hour, minute
C = int(input()) ## cooking_time

H = (B+C)//60

print((A+H)%24, (B+C)%60)