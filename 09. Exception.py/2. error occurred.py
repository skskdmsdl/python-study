# 에러 발생시키기

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("첫 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >=10:
        raise ValueError
    print(f"{num1} / {num2} = {int(num1 / num2)}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


### 추가 공부 ###
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! pass')
    else:
        raise ValueError
except ValueError:
    print('Raise! Occurred ValueError')
except Exception:
    print('Occurred Exception')
else:
    print('ok! else!')
