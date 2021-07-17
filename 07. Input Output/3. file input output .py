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