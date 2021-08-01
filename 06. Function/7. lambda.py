# 람다식
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화

# def mul_10(num):
#     return num * 10

# def mul_10_one(num): return num * 10
#
# lambda x: x * 10

# 일반적 함수 -> 변수 할당
def mul_10(num):
    return num * 10

mul_func = mul_10

print(mul_func(5))
print(mul_func(6))

# 람다 함수 -> 할당
lambda_mul_func = lambda x: x * 10

print(lambda_mul_func(20))

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_func)
func_final(10, 10, lambda x: x * 1)