cnt = int(input())

for i in range(0,cnt):
    result = ''
    num, text = input().split()
    num = int(num)
    
    for j in range(0,len(text)):
        result += text[j]*num

    print(result)