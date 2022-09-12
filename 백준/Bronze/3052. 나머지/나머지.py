nums = list()

while True:
    try:
        nums.append(int(input()) % 42)
    except:
        break
        
print(len(set(nums)))