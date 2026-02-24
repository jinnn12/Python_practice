class FourCal:
    # def setData(self, first, second): # 클래스 내부의 함수는 메서드라고 칭한다
    #     self.first = first
    #     self.second = second

    # __init__은 객체.setData를 활용하지 않고도 a.FourCal(4, 2)와 같이 변수 선언을 할 수 있다.
    def __init__(self, first, second):  # __init__은 초기화 역할을 한다, 초기 생성자
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
print(a.add()) # 6
print(a.mul()) # 8
print(a.sub()) # 2
print(a.div()) # 2

b = FourCal(3, 7)

# 클래스의 상속 : 부모클래스가 '라이브러리 형태' 혹은 '수정이 허용되지 않는' 상황이라면 상속을 사용해야 한다.
class MoreFourCal(FourCal): # 파이썬에서의 상속은 '클래스(상속할 부모클래스명)' 으로 정의한다
    def pow(self):
        result = self.first ** self.second
        return result

c = MoreFourCal(4, 2)
print(c.add())
print(c.pow())

class SafeFourCal(FourCal): # 메서드 오버라이딩, 부모클래스 메서드를 여기서 재정의함
    def div(self):
        if self.second == 0:
            return "0으로는 나눌 수 없습니다."
        else:
            return self.first / self.second

d = SafeFourCal(4, 0)
print(d.div())

class Family:
    lastName = "park" # 클래스변수의 경우 변경 시 모든 객체에 공유 된다

print(Family.lastName)
e = Family()
f = Family()
e.lastName = '최' # 객체변수는 클래스변수와 동일한 이름으로 생성할 수 있다.
print(e.lastName) # 최 출력
print(f.lastName) # park 출력
