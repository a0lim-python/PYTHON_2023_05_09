N = int(input())
num_5 = N//5
left = N%5

while left%3 != 0:
    num_5 -= 1
    if num_5 < 0:
        print(-1)
        break
    else:
        left = N - 5*num_5
else:
    num_3 = left//3
    print(num_5 + num_3)