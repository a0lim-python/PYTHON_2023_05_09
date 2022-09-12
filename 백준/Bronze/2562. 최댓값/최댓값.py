M = 0
nums = list()
while True:
    try:
        nums.append(int(input()))
    except:
        break

print(max(nums))
print(nums.index(max(nums)) + 1)