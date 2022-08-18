import math

N = int(input())

start = 2

if N > 1:
    while N >= start:
        if N % start == 0:
            print(start)
            N = N // start
            start = 2
        else:
            start += 1