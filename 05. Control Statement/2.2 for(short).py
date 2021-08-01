# 한 줄 for문 (list comprehension)

# 출석번호 1, 2, 3, 4 앞에 100을 붙이기로 함 👉 101, 102, 103, 104
students = [1,2,3,4]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

### 추가 공부 ###
numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)

numbers2 = [x for x in range(1, 101)] # 맨 앞의 x는 apppend됨
print(numbers2)