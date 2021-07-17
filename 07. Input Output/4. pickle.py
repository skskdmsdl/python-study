# pickle

import pickle

# pickle을 쓰기위해서는 b를 적어 바이너리 타입임을 적어줘야함("wb")
# 또한 따로 인코딩 설정이 필요 없음
profile_file = open("profile.pickle", "wb") # 파일 쓰기
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # 파일 읽기
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()