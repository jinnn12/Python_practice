# 집합 1. 자료형, set 키워드를 통해 만들 수 있다.
# s1 = set([1, 2, 3])
# print(s1) # {1, 2, 3}
#
# 중복 허용 X, 순서가 없음 -> 중복 제거용 필터
# 리스트 / 튜플은 순서 보장 O
# s2 = set('hello')
# print(s2)
#
# 중괄호를 활용해 set 키워드 없이 직접 집합 자료형을 만들 수 있다.
# s3 = {"apple", "banana", "cherry", 1, 100}
# print(s3)
#
# 집합 자료형의 인덱싱 접근 -> 리스트 / 튜플로 형 변환 후 진행해야 함
# s4 = set([1, 2, 3])
# l1 = list(s4)
# print(l1)
# print(l1[0])
#
# t1 = tuple(s4)
# print(t1)
# print(t1[1])
#
#
# # 교집합 / 합집합 / 차집합 구하기
# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8 ,9])
#
# # 교집합 연산자: &
# print(s1 & s2) # 이것도 set 자료구조이기 때문에 순서 보장 X
# # intersection 함수를 통해 교집합을 얻을 수도 있다
# print(s1.intersection(s2))
#
# # 합집합 연산자: |
# print(s1 | s2)
# # union 함수를 통해 합집합을 얻을 수도 있다.
# print(s1.union(s2))
#
# # 차집합 연산자: -
# print(s1 - s2) # {1, 2, 3}, 당연히 순서보장 X
# print(s2 - s1) # {7, 8, 9}, 당연히 순서보장 X
# # difference 함수를 통해 차집합을 얻을 수도 있다.
# s1.difference(s2)
# s2.difference(s1)
#
# 값 1개 추가하기, add
# s1 = set([1, 2, 3])
# s1.add(4)
# print(s1)
#
# 값 여러개 추가하기, update
# s1 = set([1, 2, 34, 6])
# s1.update([12, 8, 7])
# print(s1)

# 특정 값 제거하기: remove
# s1 = set([1, 2, 3])
# s1.remove(2)
# print(s1)
# --> 없는 값을 제거할 경우 TraceBack 에러 발생

# 특정 값 제거하기: discard
s1 = set([1, 2, 3, 4])
s1.discard(6)
print(s1)
# --> 없는 값을 제거하는 경우에 에러 발생 X

# 모든 값 제거하기: clear
s2 = set([1, 3, 5, 7])
s2.clear()
print(s2)
# --> 빈 객체 리턴 방식: set()
# 내가 예상한 건 clear 됐으니, {}이 리턴돼야 하는데, 이미 빈 딕셔너리의 리턴값이 {}이므로 set()으로 리턴한다.

