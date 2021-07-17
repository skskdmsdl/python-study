import pickle

# 좀 더 간편하게 파일 입출력이 가능
# close 필요 없이 자동으로 출력해줌
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())