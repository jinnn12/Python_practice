# 1. 1. 문자열 더하기
# head = "Python"
# tail = " is fun!"
# print(head + tail)
#
# # 1. 1. 문자열 개수 세는 것도 이렇게 쉽다고?
# a = "Life is too short"
# # len(a)
# print(len(a))
# print(a[3]) # 배열 인덱스번호, 즉 'e'
# print(a[-5]) # 뒤에서부터 5번째 자리의 값 : 's'
#
# # % 출력용 규칙
# # b = "Error is %d%" % 98
# b = "Error is %d%%" % 98
# print(b)
#
# # f 접두사
# name = '홍길동'
# age = 30
# fFormatting=f'나의 이름은 {name}이고, 나이는 {age}입니다.'
# print(fFormatting)
#
# age2 = 30
# fFormatting2 = f'나는 내년이면 {age2 + 1}살이 된다.'
# print(fFormatting2)
#
# d = {'name':'홍길동', 'age':30}
# fFormatting3 = f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]} ㅋㅋ'
# print(fFormatting3)
#
# commaChunk = f'난 {1500000:,} BP를 원해'
# print(commaChunk)
#
# # 1. 1. 문자열 관련 함수들
# #1. 문자 개수 세기, count
# aCount = "hobby"
# aNum = aCount.count('b')
# print(aNum)
#
# #2. 위치 알려주기, find
# # 처음으로 그 문자열이 나온 인덱싱 넘버
# bFind = "Python is the best choice"
# bNum = bFind.find('b')
# print(bFind.find('b'))
#
# ## 문자열에 없는 경우 -1을 리턴한다.
# cNum = bFind.find('k')
# print(cNum)
# print(bFind.find('k'))

#2-1. 위치 알려주기, index
# a = "Life is too short"
# print(a.index('t')) #8 리턴
#
# # 3. 1. 1. 문자열 삽입, join
# p = ",".join('abcd')
# print(p)

# d = ",".join(['a', 'b', 'c', 'd'])
# print(d)

# 4. 소문자를 대문자로 바꾸기, upper
# a = "hi"
# a = a.upper() # 원문은 변하지 않으므로, a 재정의
# print(a) # HI 출력

# 4-1. 대문자를 소문자로 바꾸기, lower
# a = "HI"
# a = a.lower()
# print(a)


# 5. 공백 지우기, lstrip / rstrip / strip
# a = " .hi"
# a = a.lstrip()
# print (a)
#
# b = " hi. "
# b = b.rstrip()
# print(b)
#
# c = ' .hi. '
# c = c.strip()
# print(c)


# 6. 1. 1. 문자열 바꾸기, replace
# a = "Life is too short"
# a = a.replace("short", "looooonnnnnggg")
# print(a)


# 7. 1. 1. 문자열 나누기, split : 문자열을 나눈 후 List 배열에 담는다
# a = "Life is too short"
# a = a.split()
# print(a)
#
# b = "a:b:c:d"
# b = b.split(":")
# print(b)


# 8. 문자열이 알파벳으로만 이루어져 있는지 확인하기, isalpha
# s = "Python"
# ss = s.isalpha()
# print(ss) # True
#
# s1 = "Python3"
# print(s1.isalpha()) # False
#
# s2 = "Python Hi!"
# print(s2.isalpha()) # False


# 8-1. 문자열이 숫자로만 이루어져 있는지 확인하기, isdigit
# s = "12345"
# print(s.isdigit()) # True
#
# s1 = "12345a"
# print(s1.isdigit()) # False


# 9. 문자열이 특정 문자(열)로 시작하는지 확인하기, startswith
# s = "Life is too short"
# print(s.startswith("Life"))
# print(s.startswith("L"))





