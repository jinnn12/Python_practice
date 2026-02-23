# 인터프리터 실행: 터미널에서 '4. 파이썬 날개달기' 이동
# python 실행
# module: 함수, 변수, 클래스를 모아놓은 '파이썬 파일(.py)'

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 1. 전체 import
# import module
# module.add(1, 2)

# 2. 특정 함수 import
# from module import add
# add(1, 2) -> 'module.'이 필요 없음
# from module import add, sub -> add, sub 모두 사용 가능
# from module import *

# print(add(1, 4))
# print(sub(4, 2))

# 직접 module 파일을 실행할 경우, __name__ 변수에는 __main__ 값이 저장된다.
# 하지만 shell / 다른 파이썬 모듈에서 import module의 경우 __name__ 변수에 'module.py'의 이름인 module이 저장된다.
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
