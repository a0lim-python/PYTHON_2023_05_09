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

## 자료형

### 파이썬 자료형

![image](https://user-images.githubusercontent.com/104348646/182744625-a14c28b2-99d0-4a57-87fa-49bad1eab66f.png)

* 숫자
  - int: 정수형(임의 정밀도)
  - cf) 임의 정밀도: 자릿수 단위로 쪼개어 배열 형태로 표현하는 무제한 자릿수의 정수형
  - bool: 논리 자료형, 내부적으로 정수 값을 가짐(True,Fale(1,0))
  - object > int > bool

* 매핑(Mapping)  
: 키와 자료형으로 구성된 복합 자료형
  - dictionary

* 집합  
  - set: 중복된 값을 갖지 않는 자료형
```
set() ## 빈 집합
a = {1,2,3,3} // {1,2,3} ## 값(1,2,3)이 포함된 집합 
```

* 시퀀스(sequence)(수열)
  - list: 다양한 값들을 배열 형태의 순서 있는 나열로 문자열을 이루는 자료형
  
* 원시 타입
  - PYTHON  
  : 원시 언어를 지원하지 않음
    + 우선순위: 편리함, 다양한 기능
   
  - C, JAVA 등의 언어
    : 원시 언어를 지원
    + 우선순위: 성능  

![image](https://user-images.githubusercontent.com/104348646/182744670-f2fa7d7d-8261-4bae-ae9b-fe89ed334110.png)

### 객체(object)
* 파이썬에서는 문자, 숫자 모두 (불변)객체

* 종류
  - 불변(immutable object)  
  : 값 변경 시 새로운 객체를 참조하여 새 메모리 주소에 저장됨
  - 가변(mutable object)

![image](https://user-images.githubusercontent.com/104348646/182744723-068e9d6a-68c7-45ff-aab9-36be964c8158.png)

* 불변 객체
    - 값을 담고 있는 변수는 참조일 뿐이고, 실제로 값을 갖고 있는 int, str은 모두 불변 객체
```
10; a=10; b=a
id(10); id(a); id(b) // 4393858752 ## 모두 동일
```

* 가변 객체
    - 다른 변수가 참조하고 있을 때 그 변수의 값 또한 변경됨
```
a = [1, 2, 3, 4, 5]
b = a // b =  [1, 2, 3, 4, 5]
a[2] = 4
a; b // [1, 2, 4, 4, 5] ## 값이 같음
```

* is VS ==
  - None  
  : 값이 정의되어 있지 않음 -> ==(X), is(O)

  - [1, 2, 3] VS list([1, 2, 3])  
  : 별도의 객체로 복사 됨 -> ==(True), is(False)

  - [1, 2, 3] VS copy.deepcopy([1, 2, 3])  
  : 별도의 객체로 복사 됨 -> ==(True), is(False)  

* 속도
  - 원시 타입  
    : 메모리에서 값을 꺼냄 -> 연산  

  ![image](https://user-images.githubusercontent.com/104348646/182745148-a24e9c8b-94ef-494b-8437-a3d100617aec.png)  

  - 파이썬의 객체  
    : 메모리에서 값 요청 -> PyObject_HEAD에서 타입 코드 찾기 -> ... -> 값을 꺼냄 -> 연산
      + cf) numpy 모듈  
      : 리스트를 C의 원시 타입으로 처리 -> 속도 빠름

* 자료구조, 자료형, 추상 자료형
    - 자료구조(Data Structure)  
    : (학문적 의미) 데이터에 효율적으로 접근하고 조작하기 위한 데이터의 조직, 관리, 저장구조
    - 자료형(Data Type)  
    : 일종의 데이터 속성(Attribute)  
      cf) 정수, 실수, 문자열 등의 원시 자료형까지 포함하는 모든 자료의 유형 
    - 추상 자료형(ADT =Abstract Data Type)  
    : 해당 유형의 자료에 대한 연산들을 명기한 것  
      cf) 행동만을 정의, 실제 구현 방법은 명시하지 않음 <-> 자료구조
