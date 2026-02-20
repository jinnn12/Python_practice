# for x in 리스트(또는 튜플, 문자열): ~

# testList = ['one', 'two', 'three']
# for i in testList:
#     print(i)

# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     print(first + last)

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number += 1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# marks = [90, 25, 84, 11, 60]
# number = 0
# for x in marks:
#     number += 1
#     if x >= 60:
#         print("%d번 학생은 굿이에요" % number)
#     else:
#         print("%d번 학생은 공부를 더하세요" % number)

# marks = [90, 25, 68, 45, 80]
#
# number = 0
# for x in marks:
#     number += 1
#     print(f"count = {number}")
#     if x < 60:
#         continue
#     print("continue")
#     print("%d번 학생 축하합니다." % number)

## range(n) : 0부터 n 미만의 숫자를 포함하는 range 객체를 만드는 함수
# a = range(10)
# print(a) ## range(0, 10) 객체 출력
#
# for i in range(10):
#     print(i) ## 0 ~ 9까지의 숫자 출력

# add = 0
# for i in range(1, 11):
#     print(i) ## 1 ~ 10까지 출력
#     add += i
# print(add) ## 1 ~ 10까지 총 더한 합, 55

# marks = [90, 25, 78, 45, 89]
# for number in range(len(marks)): ## len(marks) == 5, range(5) --> 0, 1, 2, 3, 4
#     if marks[number] < 60: ## marks[0], marks[1], marks[2], ..
#         continue
#     print("%d번 학생 합격입니다." % number)

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print(' ')

## 리스트 컴프리헨션: 리스트 내 for문을 포함
# a = [ 1, 2 ,3, 4 ]
# result = []
# for num in a:
#     result.append(a * 3)
#
# print(result)
#
# ## 리스트 컴프리헨션 사용예시
# a = [ 1, 2, 3, 4 ]
# result = [num * 3 for num in a]
# print(result)
#
# ## 짝수인 경우만 3을 곱해서 사용한다면?
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)

# for문을 2개 이상 사용하는 경우
result = [ x * y
           for x in range(2, 10)
           for y in range(1, 10)]
print(result)

## enumrate 함수 활용하기부터 시작