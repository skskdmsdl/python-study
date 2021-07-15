# 표준 입출력

print("Python", "Java")
print("Python" + "Java")
print("Python", "Java", sep=",")
print("Python", "Java", "JavaScript", sep="vs")

print("Python", "Java", sep=",", end="?") # Python,Java?무엇이 더 재밌을까요?
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력 처리
print("Python", "Java", file=sys.stderr) # 표준 에러 처리

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    # .ljust(8) 8칸 확보하고 왼쪽 정렬  / .rjust(4) 4칸 확보하고 오른쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":") 

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 3칸 확보하고 값이 없는 경우 0으로 대체

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 사용자 입력을 통해 값을 받게되면 항상 문자열 타입으로 받게 됨
print("입력하신 값은 " + answer + "입니다.")