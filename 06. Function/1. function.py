# 함수
# 함수 : 특정기능을 함(매개변수를 이용해 자료를 전달)
# 메서드 : 특정 자료와 연관지어 기능을 함(자료 뒤에 .을 찍어 사용)

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


# 전달값과 반환값

def deposit(balance, money): # 입금
    print(f"입금이 완료되었습니다. 잔액은 {balance + money}원 입니다.")
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.")
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance}원 입니다.")
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 15000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 200)
print(f"수수료는 {commission}원 이며, 잔액은 {balance}원 입니다.")

### 추가 공부 ###
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 함수 호출
# function_name()

# 함수 선언 위치 중요

# 예제1
def hello(world):
    print("Hello, ", world)

param1 = "Niceman"
hello(param1)

# 예제2
def hello_return(world):
    value = "Hello, " + str(world)
    return value

str = hello_return("Niceman")
print(str)

# 예제3(다중리턴)
def func_mul1(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1, y2, y3

val1, val2, val3 = func_mul1(3)
print(val1, val2, val3)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return (y1, y2, y3)

tup = func_mul2(4)
print(type(tup), tup, list(tup))

# 리스트 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return [y1, y2, y3]

lis = func_mul2(6)
print(type(lis), lis, set(lis))

# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return {'ret1': y1, 'ret2': y2, 'ret3': y3}

dic = func_mul3(8)
print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())

# 예제4 
# *args, **kwargs 이해

# *args : 가변인자로 매개변수를 어떻게 넣든 튜플로 넘어옴
def args_func(*args):  # 매개변수명 자유롭게 변경 가능
    for i, v in enumerate(args): # enumerate() 인덱스 생성
        print('{}'.format(i), v, end=' ')

args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')
print()

# **kwargs : 가변인자로 매개변수를 어떻게 넣든 딕셔너리로 넘어옴
def kwargs_func(**kwargs):  # 매개변수명 자유롭게 변경 가능
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v], end=' ')

kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')
print()

# 전체 혼합
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)

example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)

# 예제5
# 중첩함수(클로저) -> 이후 파이썬 데코레이터 클로저까지 공부하기
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In func")
    func_in_func(num + 100)

nested_func(1)

# 실행불가
# func_in_func(1)

# 예제6
# Hint
def func_hint(x : int) -> list:
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return [y1, y2, y3]
print(func_hint(2))

def tot_length1(word: str, num: int) -> int:
    return len(word) * num
print('hint exam1 : ', tot_length1("i love you", 10))

def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)
tot_length2("niceman", 10)
