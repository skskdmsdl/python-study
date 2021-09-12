# pandas
# 구조화된 데이터를 효과적으로 처리하고 저장
# Array 계산에 특화된 NumPy를 기반으로 설계 : Data와 Index를 가지고 있음

import padas as pd

data = pd.Series([1, 2, 3, 4])
print(data)

# dtype 인자로 데이터 타입을 지정할 수 있음
import pandas as pd

data = pd.Series([1, 2, 3, 4], dtype = "float")
print(data.dtype) # float64
