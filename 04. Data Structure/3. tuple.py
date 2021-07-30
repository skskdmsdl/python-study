# 튜플(tuple)
# list와 다르게 내용 변경이나 추가가 불가능하지만 속도가 빠름

menu = ("돈까스", "치즈돈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 에러남

# name = "유재석"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("유재석", 20, "코딩")
print(name, age, hobby)

### 추가 공부 ###
# 튜플 자료형(순서O, 중복O, 수정X,삭제X)

# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, 'Pen', 'Cap', 'Plate')
e = (10, 100, ('Pen', 'Cap', 'Plate'))

# 인덱싱
print('#=====#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][1][4])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('#=====#')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', 3 in a)
print('a - ', a.index(5))
print('a - ', a.count(4))