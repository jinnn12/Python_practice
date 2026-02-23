# # 사용자 입력 활용하기: input(), input은 입력되는 모든 값들을 문자열로 취급
# a = input()
# print(a)

# 사용자 입력 프롬프트
# a = input("숫자를 입력하세요: ")
# print(a)
# print(type(a)) # <class 'str'> 반환. 즉, 모든 입력값을 문자열로 취급

# # 정수로 변환하기
# age = input('나이를 입력하세요: ')
# age = int(age) # int 변환, 자바의 parseInt
# print(age + 1)
# print(type(age)) # <class 'int'> 리턴

# # 실수로 변환하기
# height = input("키를 입력하세요(cm): ")
# height = float(height) # 입력한 문자열을 실수로 변환
# print(height / 100) # 미터 단위로 변환

# # 한 번에 작성하기 : input과 int(float)를 한 줄에 작성할 수도 있다.
# age = int(input("나이를 입력하세요: "))
# print(age)
# print(type(age))

# print 자세히 알기
# a = 123
# print(a)
# b = "python"
# print(b)
# c = [ 1, 2, 3 ]
# print(c)

# print("life" "is" "too short")
# print("life" + "is" + "too short")
#
# # 문자열 띄어쓰기는 '쉼표(,)'로 한다.
# print('life', 'is', 'too', 'short')
#
# # sep 매개변수로 구분자 설정하기
# print('2000', '05', '23', sep='-')
# print("점프", "투", "python", sep=" t0o ")
#
# # 한 줄에 결괏값 출력하기
# for i in range(10):
#     print(i, end=' ')

# ## 간단한 계산기
# print("--- 간단한 계산기 ---")
# num1 = float(input("첫 번째 숫자를 입력하세요: "))
# num2 = float(input("두 번째 숫자를 입력하세요: "))
#
# print(f"{num1} + {num2}: {num1 + num2}")
# print(f"{num1} - {num2}: {num1 - num2}")
# print(f"{num1} * {num2}: {num1 * num2}")
# if num2 != 0:
#     print(f"{num1} / {num2}: {num1 / num2}")
# else:
#     print("0으로는 나눌 수 없습니다.")

