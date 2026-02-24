# 프로그램이 종료되지 않는 유연한 에러 처리 방법
# 1. try-except 문
# 1-1. try-except만 사용
try:
    pass
except:
    pass

# 1-2. try-except 발생오류
try:
    pass
except TimeoutError:
    pass

# 1-3. try-except 발생오류 as 오류변수
try:
    pass
except ZeroDivisionError as e:
    print(e)

# try-finally
# finally문은 try 수행 도중 예외 상관 없이 항상 수행된다. 보통 사용한 리소스를 close 할 때 많이 사용된다.
try:
    f = open('foo.txt', 'w')
    pass
finally:
    f.close()

# many error
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱싱 할 수 없습니다.')

try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as z:
    print(z)
except IndexError as i:
    print(i)

# try-else
try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print('미성년자는 출입금지')
    else:
        print('환영합니다.')

# 오류 일부러 발생시키기
class Bird():
    def fly(self):
        raise NotImplemented

class Eagle(Bird):
    def fly(self):
        print("eagles can fly very fast")

eagle = Eagle()
eagle.fly()