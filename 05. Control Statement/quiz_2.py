# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# a1
for k in q1.keys():
    if k == "가을":
        print(q1[k])
# a2
for k, v in q1.items():
    if k == "가을":
        print(v)

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
#print( q1.items() in "사과")
for  k, v in q2.items():
    if k =='사과' or v =='사과':
        print(k, v)
        break
else:
    print('포함되지 않았습니다.')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 100
# a1
if 80 < score <= 100:
    print('A학점') 
elif 60 < score <= 80:
    print('B학점') 
elif 40 < score <= 60:
    print('C학점') 
elif 20 < score <= 40:
    print('D학점') 
elif 0 <= score <= 20:
    print('E학점') 
#a2
if score >= 81:
    print('A학점') 
elif score >= 61:
    print('B학점') 
elif score >= 41:
    print('C학점') 
elif score >= 21:
    print('D학점') 
else:
    print('E학점') 

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 12, 6, 18
# a1
if a > b and a > c:
    print("a ", a)
elif b > a and b > c:
    print("b ", b)
else:
    print("c ", c)
# a2
best = a

if b > a:
    best = b
if c > best:
    best = c
print("best : ", best)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
num = '123456-2000000'
# a1
if num[7] == '2' or num[7] == '4':
    print('여자')
else:
    print('남자')
# a2
if int(num[7]) % 2 != 1:
    print('여자')
else:
    print('남자')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
# a1
for l in q3:
    if l =='정':
        continue
    print(l, end="")
print()

# a2(list comprehension)
l = [x for x in q3 if x != '정'] 
print(l)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
# a1
for num in range(0, 101):
    if num % 2 != 0:
        print(num, end=", ")
print()

# a2(list comprehension)
l = [x for x in range(0, 101) if x % 2 != 0]
print(l)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for l in q4:
    if len(l) >= 5:
        print(l)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
# a1
for l in q5:
    if l == l.lower():
        print(l, end=" ")
print()

# a2
for l in q5:
    if l.islower():
        print(l, end=" ")
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for l in q6:
    if l.islower():
        print(l.upper(), end=" ")
    else:
        print(l.lower(), end=" ")