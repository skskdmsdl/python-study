# 집합(set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "정형돈"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)

### 추가 공부 ###
# 집합(Sets) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환
l = list(c)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('l - ', s1 & s2)
print('l - ', s1.intersection(s2))

# 합집합
print('l - ', s1 | s2)
print('l - ', s1.union(s2))

# 차집합
print('l - ', s1 - s2)
print('l - ', s1.difference(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)