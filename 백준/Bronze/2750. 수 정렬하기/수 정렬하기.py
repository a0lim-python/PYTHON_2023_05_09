N = int(input())
l = list()
while True:
    try:
        l.append(int(input()))
    except:
        break
        
l.sort() ## 오름차순 정렬
for i in l:
    print(i)