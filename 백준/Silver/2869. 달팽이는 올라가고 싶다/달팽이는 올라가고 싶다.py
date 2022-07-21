import math

A, B, V = map(int, input().split(' '))

day_1 = (V-A)/(A-B) ## days during snail go up to V (except day 1)
day_1 = math.ceil(day_1)

day = day_1 + 1 ## reflect day 1
print(day)