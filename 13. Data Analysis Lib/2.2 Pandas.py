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
