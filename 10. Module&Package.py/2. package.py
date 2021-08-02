# 패키지
# 모듈들을 모아놓은 집합

import travel.thailand # 맨 뒤에는 모듈, 패키지만 가능(클래스나 함수는 안됨)
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from import에서는 클래스 가져오기 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# from random import *
from travel import * # __init__에 vietnam 모듈 설정 해줘야 오류 안남
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()


### 추가 공부 ###
# 파이썬 모듈과 패키지

# 패키지 예제1
# 상대 경로 패키지
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(100)

print("ex1 : ", Fibonacci.fib2(200))
print("ex1 : ", Fibonacci().title) # 클래스 생성(인스턴스화) 시켜줘야 init메소드 호출됨


# 사용2(클래스) - 메모리를 많이 사용하기에 권장하지 않음
from pkg.fibonacci import *

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)


# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(500)

print("ex3 : ", fb.fib2(600))
print("ex3 : ", fb().title)


# 사용4(함수) : 파일 Alias
import pkg.calculations as c

print("ex4 : ", c.add(10,10))
print("ex4 : ", c.mul(10,4))


# 사용5(함수)
from pkg.calculations import div as d

print("ex5 : ", int(d(100,10)))


# 사용6
import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(p))
print(dir(builtins))