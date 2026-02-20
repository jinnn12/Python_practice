# # bool: 항상 두 개의 값인 True / False (첫 글자는 무조건 대문자로 해야함)
# a = True
# b = False
# print(type(a)) # <class 'bool'> 리턴
#
# print(1 == 1) # True 리턴
# print(1 > 2) # False 리턴
# # 문자열, 리스트, 튜플, 딕셔너리 값이 비어 있으면 거짓(False)를 리턴, 비어 있지 않으면 참이 된다.
# # 숫자에서는 값이 0일 때 거짓을 리턴한다. None은 거짓을 의미한다
#
# l1 = [1, 2, 3, 4]
# while l1:
#     print(l1.pop())
#
# if []:
#     print("참")
# else:
#     print("거짓")
#
# if [1, 2, 23]:
#     print("참")
# else:
#     print("거짓")

# 불 연산
print(bool('python'))
print(bool(''))

print(bool([1,2,3]))
print(bool([]))

print(bool(3))
print(bool(0))
