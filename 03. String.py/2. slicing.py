# 슬라이싱(인덱싱)

rrn = "990102-1234567"

print("성별 : " + rrn[7])
print("년도 : " + rrn[0:2]) # 0 부터 2 직전까지 (0, 1)
print("월 : " + rrn[2:4]) 
print("일 : " + rrn[4:6]) 
print("생년월일 : " + rrn[0:6])  

print("생년월일 : " + rrn[:6])  # 처음부터 6 직전까지
print("뒤 7자리 : " + rrn[7:])  # 7 부터 끝까지
print("뒤 7자리(뒤에서부터) : " + rrn[-7:])  # 맨 뒤에서 7번째부터 끝까지

# 일부분 추출(정말 중요)
str_sl = 'Niceboy'

# 슬라이싱 연습
print(str_sl[0:3])
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-3:6])
print(str_sl[1:-2])
print(str_sl[::-1]) # revers와 비슷한 결과
print(str_sl[::2])

# immutable 삭제
del str_sl

# 아스키코드
a = 't'

print(ord(a))
print(chr(116))