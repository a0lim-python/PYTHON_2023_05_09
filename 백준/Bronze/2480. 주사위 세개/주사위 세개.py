import collections

dice = list(map(int, input().split()))
stat = collections.Counter(dice)
most = stat.most_common()[0] ## num, count

if most[1] == 3:
    print(10000 + most[0] * 1000)
elif most[1] == 2:
    print(1000 + most[0] * 100)
else:
    print(max(stat) * 100)