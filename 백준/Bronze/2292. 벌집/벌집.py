N = int(input()) ## count of room
N_th = 1 ## answer
max = 1 ## max num in condition(1/2~7/8~19/...)

while N > max: 
    max += 6*N_th ## move to nex condition
    N_th +=1
    
print(N_th)