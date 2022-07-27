## itertools

### 1. accumulate

#### 누적합 연산
```
k = [1, 2, 3, 4]
list(itertools.accumulate(k))
// [1, 3, 6, 10]
```
#### 누적곱 연산
```
import operator
k = [1,2,3,4]
list(itertools.accumulate(k, operator.mul))
// [1,2,6,24]
```
