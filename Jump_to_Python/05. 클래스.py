# 클래스(class) : ex. 과자틀
# 객체(object) : 클래스로 만든 피조물, 객체마다 고유한 성격(다른 객체에 영향을 주지 않음) ex. 과자

# ex. 기존의 계산기 생성 및 실행: 계산기가 각각의 결과값을 유지 필요
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# ex. 클래스: 계산기(함수) 반복 생성 및 실행 가능
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator() # 객체
cal2 = Calculator()

print(cal1.add(3)) # 다른 계산기의 결과값과 상관 없이 독립적인 값 유지
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 기본 클래스(클래스 -> 객체 -> 인스턴스 만듦)
class Cookie: # 기능x, 객체 생성 가능
    pass
a=Cookie() # 객체 a
b=Cookie() # 객체 b

# 사칙연산 클래스(FourCal)
## 구조 시안
a = FourCal() # 객체 a 생성
a.setdata(4,2) # 숫자 지정
print(a.add()) # 사칙연산 수행

class FourCal:
    def setdata(self, first, second): # 메서드(Method): 클래스 안에 구현된 함수 # 매서드의 매개변수
        #첫번째 매개변수 self는 객체를 호출 시 호출한 객체 자신이 전달
        self.first = first # 메서드의 수행문
        self.second = second #메서드의 수행문
    def add(self): # + 기능 추가
        result=self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(4,2) # a=self / 4=first / 2=second
a.setdata(self,4,2) # 위와 동일하게 출력됨
a.add()

