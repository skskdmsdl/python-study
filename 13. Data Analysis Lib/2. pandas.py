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


# DataFrame
# 여러 개의 Series가 모여서 행과 열을 이룬 데이터
gdp_dict = {
  'china': 1409250000,
  'japan': 516700000,
  'korea': 169320000,
  'usa': 2041280000,
}
gdp = pd.Series(gdp_dict)


country = pd.DataFrame({
  'gdp': gdp,
  'population': population
})


# Dictionary를 활용하여 DataFrame 생성 가능
data = {
  'country': ['china', 'japan',
  'korea'
  ,
  'usa'],
  'gdp': [1409250000, 516700000, 169320000, 2041280000],
  'population': [141500, 12718, 5180, 32676]
}

country = pd.DataFrame(data)
country = country.set_index('country')


# DataFrame 속성을 확인하는 방법
print(country.shape) # (4, 2)
print(country.size) # 8
print(country.ndim) # 2
print(country.values) # [[1409250000 141500] 
                      # [ 516700000 12718] 
                      # [ 169320000 5180] 
                      # [2041280000 32676]]
 

# DataFrame의 index와 column에 이름 지정
country.index.name = "Country" # 인덱스에 이름 지정
country.columns.name = "Info" # 컬럼에 이름 지정
print(country.index)
# Index(['china', 'japan', 'korea', 'usa'], dtype='object', name='Country’)
print(country.columns)
# Index(['gdp', 'population'], dtype='object', name='Info')


# 데이터 프레임 저장 및 불러오기 가능
country.to_csv("./country.csv")
country.to_excel("country.xlsx")
country = pd.read_csv("./country.csv")
country = pd.read_excel("country.xlsx")


# 데이터 선택 및 변경하기
# .loc : 명시적인 인덱스를 참조하는 인덱싱/슬라이싱
country.loc['china'] # 인덱싱
country.loc['japan':'korea', :'population'] # 슬라이싱


# .iloc : 파이썬 스타일의 정수 인덱스 인덱싱/슬라이싱
country.iloc[0] # 인덱싱
country.iloc[1:3, :2] # 슬라이싱


# 컬럼명 활용하여 DataFrame에서 데이터 선택 가능
country
country['gdp']
country[['gdp']]


# Masking 연산이나 query 함수를 활용하여 조건에 맞는 DataFrame 행 추출 가능
country[country['population'] < 10000] # masking 연산 활용
country.query("population > 100000") # query 함수 활용


# Series도 numpy array처럼 연산자 활용 가능
gdp_per_capita = country['gdp'] / country['population']
country['gdp per capita'] = gdp_per_capita
