# Pandas 심화

# Index 값 기준으로 정렬하기
# axis = 0 : 행 인덱스 기준 정렬(Default 오름차순)
df = df.sort_index(axis = 0)

# axis = 1 : 열 인덱스 기준 내림차순 정렬
df.sort_index(axis = 1, ascending = False)


# Column 값 기준으로 정렬하기
# col1 컬럼 기준 정렬(Default 오름차순)
df.sort_values('col1', ascending = True)

# col1 컬럼 기준 내림차순 정렬
df.sort_values('col1', ascending = False)

# col2 컬럼 기준 오름차순 정렬 후 col2 컬럼 기준 내림차순 정렬
df.sort_values(['col2', 'col1'], ascending = [True, False])


# 데이터프레임 분석용 함수
# count 메서드 활용하여 데이터 개수 확인 가능
# (Default : NaN값 제외)
data = {
  'korean': [50, 60, 70],
  'math': [10, np.nan, 40]
}
df = pd.DataFrame(data, index = ['a','b','c'])
df.count(axis = 0) # 열 기준
df.count(axis = 1) # 행 기준

# max, min 메서드 활용하여 최대, 최소값 확인 가능
# (Default : 열 기준, NaN값 제외)
ata = {
  'korean': [50, 60, 70],
  'math': [10, np.nan, 40]
}
df = pd.DataFrame(data, index = ['a','b','c'])
df.max() # 최댓값
df.min() # 최솟값
