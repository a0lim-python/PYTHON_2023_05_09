## 백준에서만 안 됨
import re ## library problem??

word = input()

word = re.sub('-|=', '', word) ## delete -, =
word = re.sub('dz|lj|nj', '*', word) ## make to one alphabet(*)

print(len(word))