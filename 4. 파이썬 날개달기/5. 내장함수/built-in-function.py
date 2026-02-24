# map
# map (함수, 반복가능한 데이터)

# two times 함수
def two_times1(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times1([1, 2, 3, 4])
print(result)

# map 함수를 활용하여 바꿔보자
def two_times2(x):
    return x * 2

print(list(map(two_times2, [1, 2, 3, 4])))
