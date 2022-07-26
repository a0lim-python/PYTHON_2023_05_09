# NOT SOLVED

T = int(input())


for t in range(0,T):
    
    R, S = input().split()
    R = int(R)
    answer = list()
    
    for i in range(0, len(S)):
        rep = S[i] * R
        answer.append(rep)
        
    print(answer)