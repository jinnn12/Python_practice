# dictionary는 말 그대로 사전을 의미한다.
# Key: Value 형태로 이루어져 있다.
# {Key: Value, Key: Value, ...}

# 딕셔너리 쌍 추가하기
a = {'name': 'James'}
a['job'] = 'Engineer'
print(a)
# 기존 {'name': 'James'} 딕셔너리에서 {'job': 'Engineer'} Key: Value를 추가한 것이다.
print(a.get('name'))
print(a['job'])
print(a.setdefault('coffee', 'flower'))

# dic.keys() -> key들을 dict_keys 객체로 반환한다.
b = a.keys()

print(b) # dict_keys(['name', 'job'])
print(list(b)) # list(b)를 통해 dict_kesy 객체를 list로 변환할 수 있다.

# dic.items() -> Key:Value 쌍을 dict_items 객체로 얻을 수 있다
c = a.items()
print(c)
print(list(c))

# Key로 Value 값 가져오기, .get(Key) == a[Key]
print(a.get('coffee'))

# Key의 존재여부, in
dic = {'name':'pey', 'phone':'010-1111-1234', 'birth':'1120'}
print('name' in dic) # True
print('email' in dic) # False

# Key로 Value 리턴 후, 딕셔너리에서 삭제 : pop(Key)
dic.pop('name')
print(dic)
print(dic.pop('birth'))
print(dic)





