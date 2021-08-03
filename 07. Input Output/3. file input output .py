# 파일 입출력

score_file = open("score.txt", "w", encoding="utf8") # w 파일 쓰기 용도(write)
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # a 추가해서 쓰기 용도(append)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r 읽기 용도
print(score_file.read()) # 한 번에 모든 내용 불러오기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r 읽기 용도
print(score_file.readline()) # 라인별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r 읽기 용도
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r 읽기 용도
lines = score_file.readlines() # 모든 라인 가져와서 list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()


### 추가 공부 ###
# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
contents = f.read()
print(contents)
# print(dir(f))
# 반드시 close 리소스 반환
f.close()

print()

# 예제2 - with문은 close를 해주지 않아도 됨
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(iter(c))
    print(list(c))
    print(c)

print()

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        # print(c)
        print(c.strip()) # .strip() 양쪽 공백, 줄바꿈 제거

print()


# 예제4
# read : 전체 내용 읽기, read(10) : 10글자 읽기
with open('./resource/review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)
    contents = f.read()
    print('>', contents)  # 내용 없음
    f.seek(0, 0)
    contents = f.read()
    print('>', contents)

print()

# 예제5
# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

print()

# 예제6
# readlines : 전체 읽은 후 라인 단위 리스트 저장
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c, end='')

print()

# 예제7
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)
    print('Average : {:6.3f}'.format(sum(score) / len(score)))


# 파일 쓰기
# 예제1
with open('./resource/test.txt', 'w') as f:
    f.write('niceman!')

# 예제2
with open('./resource/test.txt', 'a') as f:
    f.write('niceman!!')

# 예제3
from random import randint

with open('./resource/score2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(50, 100)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5 (자주 사용하진 않지만 알아두면 좋음)
with open('./resource/test3.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)