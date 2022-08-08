H, M = map(int, input().split())

if H == 0 and M < 45:
    print(23, M+60-45)
else:    
    if M >= 45:
        print(H, M-45)
    else:
        print(H-1, M+60-45)