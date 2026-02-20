# # 메모리 주소 확인 함수: id(객체의 주소 값 반환)
# l1 = [1, 2, 3]
# print(id(l1))
#
# # 리스트 복사
# a = [1, 2, 3]
# b = a
# # b는 a와 완전 동일한가?
# print(id(a))
# print(id(b))
#
# # is 연산자: a와 b가 가리키는 객체가 같을까?
# print(a is b)

#------------------#
# a = [1, 2, 3]
# b = a
# a[1] = 4
# print(a) # [1, 4, 3]
# print(b) # [1, 4, 3]
# b도 똑같이 바뀌었음, 참조 메모리가 똑같기 때문이다

# a = [1, 2, 3]
# b = a[:] # 리스트 전체를 가리키는 ':' 연산을 사용하여 복사
# a[1] = 4
# print(a) # [1, 4, 3]
# print(b) # [1, 2, 3] -> b리스트에는 영향이 생기지 않음, 참조 메모리가 다름
# print(a is b) -> False

# b = a[:]와 동일
# from copy import copy
# a = [1, 2, 3]
# b = copy(a)

# 튜플로 a, b에 값을 대입
a, b = ('tuple', 'python')
(a, b) = ('tuple', 'python')
c, d = 'tuple2', 'pythonic' # 가장 Pythonic
print(a, b)


