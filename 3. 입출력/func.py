# 4-1 함수
# 파이썬 함수의 구조, def
# def 함수_이름(매개변수) :
#   수행할 문장 1 ..

# def add(a, b): # a와 b는 매개변수
#     return a + b
#
# a = 3
# b = 4
# print(add(a, b))
# print(add(3, 4)) # 3과 4는 인수

# def add(a, b):
#     result = a + b
#     return result

# # 입력값이 없는 함수
# def say():
#     return "멍멍"
# a = say()
# print(a)

# # 반환값이 없는 함수
# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a + b))
#
# a = add (3, 4)
# print(a)

# 입력값도, 반환값도 없는 함수, 함수_이름()
# def say():
#     print("hi!")
# say()

# def sub(a , b):
#     return a - b
#
# result = sub(a = 7, b = 3)
# print(result)

# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
# res = add_many(1,2,3)
# print(res)
#
# 여러개의 입력값을 받는 함수 만들기 (*매개변수), (*args)가 관용어로 사용된다
# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result += i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result *= i
#     return result
#
# ress = add_mul("add", 1, 2, 3, 4)
# print(ress)
#
# ress2 = add_mul("mul", 1, 2, 3, 4, 5)
# print(ress2)

# 키워드 매개변수, kwargs
# def print_kwargs(**kwargs):
#     print(kwargs)
#
# print_kwargs(a=1) # {'a': 1}
# print_kwargs(name = 'foo', age = 3) # {'name': 'foo', 'age': 3}
# print_kwargs(name = "홍길동", age = 25, city = '서울', job = '프리랜서') # {'name': '홍길동', 'age': 25, 'city': '서울', 'job': '프리랜서'}
#
# def create_profile(**info):
#     print("=== 프로필 정보 ===")
#     for key, value in info.items():
#         print(f"{key}: {value}")
#
# create_profile(name = "홍길동", age = 25, city = '서울', job = '프리랜서')

# def mixed_function(name, *args, **kwargs):
#     print(f"이름: {name}")
#     print(f"추가 인수들: {args}")
#     print(f"키워드 인수들: {kwargs}")
#
# mixed_function('홍길동', 1, 2, 3, age=25, city='서울')

# # 함수의 리턴값은 언제나 '하나'이다.
# def add_and_mul(a, b):
#     return a + b, a * b
# result = add_and_mul(3, 4)
# print(result) # (7, 12) '하나'의 튜플값이 리턴된다
# # 만약 a + b, a * b 두 개의 리턴값을 가지고 싶다면?
# result1, result2 = add_and_mul(3, 4)
# print(result1)
# print(result2)
#
# # return은 한 번만 실행되기 때문에 특정 상황에서 함수를 빠져나가고 싶을 때 함수를 즉시 빠져나갈 수 있다.
# def say_nick(nick):
#     if nick == '바보':
#         return
#     print(f"나의 별명은 '{nick}'입니다.")
#
# say_nick('바')

# def say_myself(name, age, man=True):
#     print('나의 이름은 %s 입니다.' % name)
#     print('나이는 %d 입니다.' % age)
#     if man:
#         print('성별은 남자입니다.')
#     else:
#         print('성별은 여자입니다.')
#
# say_myself('진호', 27)
# say_myself('진호', 27, False)
#
# def say_myself_2(name, man=True, age):
#     print("나의 이름은 %s 입니다." % name)
#     print('나의 나이는 %d 입니다.' % age)
#     if man:
#         print('남자입니다.')
#     else:
#         print('여자입니다.')
#         ## 이는 오류가 발생한다, '초기화'하고 싶은 매개변수는 항상 뒤쪽에 놓아야 한다.

# a = 1
# def vartest(a):
#     a += 1
# vartest(a)
# print(a) # 2가 출력될 것 같으나, 1이 출력된다. 함수 내 a는 함수만의 변수이다.

# case 1) 함수 내 return 활용하기
# a = 1
# def vartest(a):
#     a += 1
#     return a
# a = vartest(a)
# print(a)

# case 2) global 명령어 사용하기, 하지만 프로그래밍에서 함수의 독립성을 보장하기 위해 global 명령어는 피하는 것이 좋다.
# a = 1
# def vartest():
#     global a # 함수 밖의 a 변수를 직접 사용하겠다
#     a += 1
# vartest()
# print(a)

# # 리스트나 딕셔너리(Key: Value)는 함수에서 변경 가능하다.
# def change_list(my_list):
#     my_list.append(4)
#
# a = [1, 2, 3]
# change_list(a)
# print(a)
#
# # lambda 예약어: def를 사용해야 될 정도로 복잡하지 않거나, def를 사용할 수 없는 곳에 주로 쓰인다.
# # 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
# add = lambda a, b : a + b # 람다로 만든 함수는 return이 없어도 표현식의 결괏값을 반환한다.
# result = add(3, 4)
# print(result)

# 함수의 독스트링(Docstring): 함수에 대한 설명을 문서화 하는 방법이 독스트링이다, 함수의 첫번째 줄에 """로 둘러싼 문자열을 작성하면 된다.
def add(a, b):
    """
    두 숫자를 더하는 함수
    :param a: 첫번째 숫자
    :param b: 두번째 숫자
    :return:
    int, float: 두 숫자의 합
    """
    return a + b
print(add.__doc__) ## 독스트링 확인하기

