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

# 배열의 데이터 타입 dtype
# 파이썬 리스트와 달리 같은 데이터 타입만 저장가능(단일 데이터)
arr = np.array([0, 1, 2, 3, 4], dtype=float)
print(arr) # [0. 1. 2. 3. 4.]
print(arr.dtype) # 'float64'
print(arr.astype(int)) # [0 1 2 3 4]

# 배열의 속성
# ndarray의 차원 관련 속성
# ndim(n + dimension) & shape

# 1차원 배열
list = [0, 1, 2, 3]
arr = np.array(list)
print(arr.ndim) # 1
print(arr.shape) # (4,) 👉 4개의 값이 하나의 행으로 존재함

# 2차원 배열
list = [[0, 1, 2] [3, 4, 5]]
arr = np.array(list)
print(arr.ndim) # 2
print(arr.shape) # (2, 3) 👉 2개의 행이 3개 열로 존재함
 

# 크기 속성
# ndarray의 크기 속성과 shape 조절

arr = np.array([0, 1, 2, 3, 4, 5])
print("arr.shape : {}".format(arr.shape)) # arr.shape : (6,)
print("배열 요소의 수 : {}".format(arr.size)) # 배열 요소의 수 : 6
print("배열의 길이 : {}".format(len(arr))) # 배열의 길이 : 1 👉 세로의 행

arr.shape = 3, 2
print("arr.shape : {}".format(arr.shape)) # arr.shape : (3,2)
print("배열 요소의 수 : {}".format(arr.size)) # 배열 요소의 수 : 6
print("배열의 길이 : {}".format(len(arr))) # 배열의 길이 : 3
