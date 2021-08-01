# for문 (반복문)

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

### 추가 공부 ###
# 기본 반복문 사용(while, for)
v1 = 1

for v2 in range(10):
    print("v2 is :", v2)

for v3 in range(1, 11):
    print("v3 is :", v3)

for v4 in range(1, 11, 2):
    print("v4 is :", v4)

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are", name)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Your number", number)

# 예제3
word = 'dreams'

for s in word:
    print('word : ', s)

# 예제4
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}

# 기본값(키)
for key in my_info:
    print(key, ":", my_info[key])

# value
for val in my_info.values():
    print(val)

# key, value
for k, v in my_info.items():
    print(k, ":", v)

# 예제5
name = 'KennRY'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# break
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : ", num)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue

    print("type:", type(v))
    print("multiply by 2:", v * 3)

# for-else 구문 (반복문이 정상적으로 수행된 경우 else 블럭 수행)
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:  # 45
        print("found : 33!")
        break
    else:
        print("not found : ", num)
else:
    print("Not Found 39...")

# 중첩 for 문 구구단 출력
for i in range(1, 11):
    for j in range(1, 11):
        print('{:4d}'.format(i * j), end='')
    print()

# 자료 구조 변환 예제
name = 'Niceman'
print('reversed : ', reversed(name))
print('list : ', list(reversed(name)))
print('list : ', tuple(reversed(name)))
print('list : ', set(reversed(name)))  # 순서X
