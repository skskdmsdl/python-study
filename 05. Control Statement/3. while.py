# while (반복문)

customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

customer = "아이언맨"
index = 1
while 0 < index <= 10:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
print("커피 가져가세요.")

### 추가 공부 ###
# 기본 반복문 사용(while, for)
v1 = 1

while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

# 1 ~ 100합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 합 : ', sum1)
print('1 ~ 100 합 : ', sum(range(1, 101)))  # sum(리스트)
print('1 ~ 100 안에 3의 배수의 합 : ', sum(range(1, 101, 3)))

# flag 사용
f = True
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

while f:
    for v in numbers:
        if v == 33:
            print("found : 33!")
            f = False
        print("not found : ", v)

# else 구문 정리(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
# 예제1
i = 1
while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1
else:
    print('else block run!')

# 예제2
j = 1
while j <= 10:
    print('j : ', j)
    if j == 11:
        break
    j += 1
else:
    print('else block run!')