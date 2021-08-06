# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect('E:/workspace/python-study/python_study/resource/database.db')  # 본인 DB 파일 경로

# 커서 바인딩 (커서 위치가 중요함)
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경 된다.
# 1개 로우 선택
print('One -> \n', c.fetchone())

# 지정 로우 선택
print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
print('All -> \n', c.fetchall())

print()

# 순회1 (이게 젤 안쓰임)
rows = c.fetchall()
for row in rows:
    print('retrieve1  >', row)  # 조회 없음

# 순회2 
for row in c.fetchall():
    print('retrieve2 >', row)  # 조회 없음

# 순회3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('retrieve3 > ', row)

print()

# WHERE Retrieve1
param1 = (1,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # 데이터 없음