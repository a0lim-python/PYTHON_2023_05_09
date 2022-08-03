## 빅오(O, big-O)
  
* 시간 복잡도(Time Complexity) (= 점근적 실행 시간= Asymptotic Running Time)  
  : 어떤 알고리즘을 수행하는 데 걸리는 시간  

* 빅오  
: 입력값이 무한대로 향할 때 함수의 상한을 설명하는 수학적 표기 방법  
    - 최고차항만을 표기. 계수는 무시  
    ex) 4*n^2+3n+4 -> 시간복잡도 = O(n^2) 

![image](https://user-images.githubusercontent.com/104348646/182528069-7eba3982-2ef1-4b6b-8f1a-e95399cb6cd6.png)

* 빅오 표기법의 종류  
![image](https://user-images.githubusercontent.com/104348646/182528913-355872e7-6e1d-4733-8e78-8ba5169c2b99.png)

![image](https://user-images.githubusercontent.com/104348646/182528153-c2c0c307-3ec0-4f75-8e08-f4bd7e9e3be2.png)

* 상한과 최악
  - 빅오(O): 상한(Upper Bound)
  - 빅세타(θ): 평균
  - 빅오메가(Ω): 하한(Lower Bound)

![image](https://user-images.githubusercontent.com/104348646/182528175-f08308d4-0afd-4bb5-8ab9-e80c2170bf18.png)

* 분할 상환 분석(Amortized Analysis)  
  : 시간/메모리를 분석하는 알고리즘의 복잡도를 계산할 때, 최악의 경우보다 알고리즘 전체를 보는 방법
    - 빅오와 함께 함수의 동작을 설명할 때 중요한 분석 방법 중 하나  
    ex) 동적 배열: 거의 발생하지 않는 더블링으로 인한 최악의 경우에 시간 복잡도가 O(n) -> 분할 상한하여 시간 복잡도를 O(1)로 계산

* 병렬화
    - 알고리즘의 병렬화로 실행 속도를 높임
    - 딥러닝, 병렬 연산을 위한 GPU 등
