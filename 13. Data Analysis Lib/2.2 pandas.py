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

# max, min 메서드 활용하여 최대, 최소값 확인 가능(Default : 열 기준, NaN값 제외)
ata = {
  'korean': [50, 60, 70],
  'math': [10, np.nan, 40]
}
df = pd.DataFrame(data, index = ['a','b','c'])
df.max() # 최댓값
df.min() # 최솟값

# sum,mean메서드활용하여합계및평균계산(Default : 열기준,NaN값제외)
data = {
  'korean': [50, 60, 70],
  'math': [10, np.nan, 40]
}
df = pd.DataFrame(data, index = ['a','b','c'])
df.sum() # 합계
df.mean() # 평균

# axis, skipna 인자 활용하여 합계 및 평균 계산(행 기준, NaN값 포함 시)
data = {
  'korean': [50, 60, 70],
  'math': [10, np.nan, 40]
}
df = pd.DataFrame(data, index = ['a','b','c'])
df.sum(axis = 1) # 합계
df.mean(axis = 1, skipna = False) # 평균

# NaN값이 존재하는 column의 평균 구하여 NaN값 대체
B_avg = df['math'].mean()
print(B_avg) # 25.0

# NaN값 대체
df['math'] = df['math'].fillna(B_avg)

# 평균
df.mean(axis = 1, skipna = False) 


# 그룹으로 묶기(group by)
# 간단한 집계를 넘어서서 조건부로 집계하고 싶은 경우
df = pd.DataFrame({
  'data1' : range(6),
  'data2' : [4,4,6,0,6,1],
  'key':['A','B','C','A','B','C']
})
df.groupby('key').sum()
df.groupby(['key','data1']).sum()

# groupby를 통해서 집계를 한번에 계산하는 방법
df.groupby('key').aggregate(['min', np.median, max])
df.groupby('key').aggregate({'data1': 'min', 'data2': np.sum})

# groupby를 통해서 그룹 속성을 기준으로 데이터 필터링
def filter_by_mean(x):
  return x['data2'].mean() > 3
df.groupby('key').mean()
df.groupby('key').filter(filter_by_mean)

# groupby를 통해서 묶인 데이터에 함수 적용
df.groupby('key').apply(lambda x: x.max() - x.min())

# groupby로 묶인 데이터에서 key값으로 데이터를 가져올 수 있음
df = pd.read_csv("./univ.csv")

# 상위 5개 데이터
df.head()

# 데이터 추출
df.groupby("시도").get_group("충남")
len(df.groupby("시도").get_group("충남"))
# 94
