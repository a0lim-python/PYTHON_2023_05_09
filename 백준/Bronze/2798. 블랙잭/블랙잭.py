N, M = map(int, input().split()) ## N = # of card / M = max of sum
card = list(map(int, input().split()))
      
answer = 0
for i in card:
    c = card[:] ## shadow copy / only c will be changed(not card) / not Homogeneous
    c.remove(i)
    for j in c:
        c.remove(j)
        for k in c:
            if i + j + k <= M and i + j + k > answer:
                answer = i + j + k
    
print(answer)
