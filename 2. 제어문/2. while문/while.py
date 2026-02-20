# treeHit = 0
# while treeHit < 10:
#     treeHit += 1
#     print("나무를 %d번 찍었습니다" % treeHit)
#     if treeHit == 10:
#         print("나무가 넘어갑니다.")

# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
#
# Enter number: """
#
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

# coffee = 10
# money = 300
# while money:
#     print("돈을 받으면 커피를 줍니다.")
#     coffee -= 1
#     print("남은 커피의 양은 %d입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다.")
#         break

# coffee = 10
# while True:
#     money = int(input("돈을 넣어주세요 : "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee -= 1
#     elif money > 300:
#         print("거스름돈 %d원을 주고 커피를 줍니다." % (money - 300))
#         coffee -= 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피는 %d잔입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 수고하세요")
#         break

# a = 0
# while a < 10:
#     a += 1
#     if a % 2 == 0: continue
#     print(a)

# count = 0
# while count < 3:
#     print(f"카운트: {count}")
#     count += 1
# else:
#     print("while문 종료")

# count = 0
# while count < 5:
#     if count == 2:
#         break
#     print(f"카운트: {count}")
#     count += 1
# else:
#     print("while문 종료")

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1