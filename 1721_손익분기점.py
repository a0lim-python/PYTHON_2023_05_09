import math

A, B, C = map(int, input().split())

if C>B:
    point = A / (C-B)
    point = math.floor(point+1) ## if point = 10, point should be 11
else: ## no point
    point = -1

print(point)
