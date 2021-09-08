# 예외처리

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError:
    print("에러! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생했습니다.")
    print(err)


### 추가 공부 ###
# 파이썬 예외처리의 이해

# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError..
# 문법적으로 에러가 없지만 코드 실행(런타임) 프로세스에서 발생하는 예외 처리 중요

# SyntaxError : 잘못된 문법

# print('test)
# print('Hello'))
# if True
#    pass
# a = 20; b = 30; a+ = b
# x => y


# NameError : 참조 변수 없음

a = 10
b = 15

# print(c)


# ZeroDivisionError : 0 나누기 에러

# print(10 / 0)


# IndexError : 인덱스 범위 오버

x = [10, 20, 30]

# print(x[1])
# print(x[3]) # 예외 발생
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) # 예외 발생
# print(x.pop(50)) # 예외 발생


# KeyError

dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}

# print(dic['hobby'])     # 키가 존재하지 않으면 예외
# print(dic.get('hobby')) # 안전


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외처리 권장(EAFP 코딩 스타일)


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

# print(time.time())
# print(time.month()) # 예외 발생

x = [1, 2, 3]
# print(x.append(4))
# print(x.add(10))


# ValueError : 참조 값이 없을 때 예외

x = [1, 5, 9]

# x.remove(5)
# print(x)

# x.remove(100)
# print(x) # 예외 발생

t = (10, 100, 1000)

print(t.index(100))
# print(t.index(7)) # 예외 발생


# FileNotFoundError

# f = open('test.txt') # 예외 발생


# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) # 예외 발생
# print(x + z) # 예외 발생
# print(y + z) # 예외 발생
# print(sum([1,2,3],10,1)) # 예외 발생

# print(x + list(y))
# print(x + list(z)
