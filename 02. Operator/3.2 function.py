# 숫자처리 함수
# 아래 URL 참조
# https://docs.python.org/3/library/math.html

print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 최대값 12
print(min(5, 12)) # 최소값 5
print(round(3.14)) # 반올림 3
print(round(4.99)) # 반올림 5

from math import *

print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3))

#외부 모듈
import math

#ceil
print(math.ceil(5.1))   # x 이상의 수 중에서 가장 작은 정수
print(math.ceil(8.999))

#floor
print(math.floor(3.874)) # x 이하의 수 중에서 가장 큰 정수
print(math.floor(-25.5))

#pi
print(math.pi)

# 2진수 변환
print(bin(50)) #0b로 시작