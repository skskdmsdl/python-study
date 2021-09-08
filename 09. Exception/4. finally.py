# finally
# 에러가 발생하든 하지 않든 무조건 실행되는 구문

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("첫 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError(f"입력값 : {num1}, {num2}")
    print(f"{num1} / {num2} = {int(num1 / num2)}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")


### 추가 공부 ###
# 예제1
try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)  # 에러 내용 출력
    # pass # 임시로 에러 해결 시 예외 처리
else:
    print('ok! else!')
finally:
    print('ok! finally!')  # 무조건 수행 됨

print()

# 예제2
# 예외처리는 하지 않지만, 무조건 수행 되는 코딩 패턴
try:
    print('try')
finally:
    print('finally')

print()
