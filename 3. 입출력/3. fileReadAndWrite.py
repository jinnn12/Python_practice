# 파일 생성 -> 내장함수 open
# r : 읽기모드 / w : 쓰기모드 / a : 추가모드
# f = open('C:/Users/user/Desktop/새파일.txt', 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다. \n" % i
#     f.write(data)
#
# f.close()

## 파일을 읽는 여러가지 방법
# case 1) readline 함수 이용하기: 가장 첫번째 줄 출력
# f = open('C:/Users/user/Desktop/새파일.txt', 'r')
# line = f.readline()
# print(line)
# f.close()
#
# f = open('C:/Users/user/Desktop/새파일.txt', 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)

# case 2) readlines 함수 이용하기:
# f = open("C:/Users/user/Desktop/새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip() # \n 개행줄 삭제 메서드
#     print(line)
# f.close()

# case 3) read 함수 사용하기, 파일의 내용 전체를 문자열로 반환
# f = open('C:/Users/user/Desktop/새파일.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# f = open('C:/Users/user/Desktop/새파일.txt', 'r')
# for line in f:
#     line = line.strip()
#     print(line)
# f.close()

# # 쓰기모드('w')로 파일을 열면 기존 내용이 모두 사라짐, 이때 내용 추가를 위해 사용 가능한 것이 추가모드('a')
# f = open('C:/Users/user/Desktop/새파일.txt', 'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다. \n" % i
#     f.write(data)
# f.close()

# with: 자동으로 파일 열기(open) / 닫기(close)
with open("C:/Users/user/Desktop/foo.txt", 'w') as f:
    f.write("Life is too short, you need python")
