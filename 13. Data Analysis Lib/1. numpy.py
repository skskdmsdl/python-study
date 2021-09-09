# Numpy(Numerical Python)
# Python에서 대규모 다차원 배열을 다룰 수 있게 도와주는 라이브러리

# Numpy를 사용하는 이유?
# 1️. 데이터를 숫자의 배열로 보고 처리하기 위해
# 2. 반복문 없이 배열 처리 가능
#    파이썬 리스트에 비해 빠른 연산을 지원하고 메모리를 효율적으로 사용 가능

import numpy as np

np_arr = np.array(range(5))
print(np_arr) # [0 1 2 3 4] -> 공백으로 구분
print(type(np_arr)) # <class 'numpy.ndarray'> -> n차원 배열
