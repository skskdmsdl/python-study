# 문자열

sectence = '나는 사람입니다.'
print(sectence)

sectence2 = "파이썬은 쉬워요"
print(sectence2)

sectence3 = """
나는 사람이고,
파이썬은 쉬워요
"""
print(sectence3)

# 문자열 생성
str1 = "I am Boy."
str2 = 'NiceMan'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 문자열 연산
str_o1 = "Niceman"
str_o2 = "Orange"
str_o3 = "this is string example....wow!!! this is really string"
str_o4 = "Kim Lee Park Joo"

print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1))
print('x' in str_o1) # x가 str_o1에 포함되어 있는지 여부(T/F)
print('i' in str_o1)
print('e' not in str_o2)
print('O' not in str_o2)

# 문자열 형 변환
print(str(77))  # type 확인
print(str(10.4))
print(str(True))
print(str(complex(12)))