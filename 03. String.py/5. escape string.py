# 탈출 문자

# \n : 줄바꿈
print("백문이 불여일견\n 백견이 불여일타")

# \" \' : 문장 내에서 따옴표
print('저는 "사람"입니다.') # 저는 "사람"입니다.
print("저는 \"사람\"입니다.") # 저는 "사람"입니다.

# \\ : 문장 내에서 \
print("E:\\workspace\\python-study")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# Raw String(경로 표시할때 사용)
raw_s1 = r'C:\Programs\python3\"'
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"

# Raw String 출력
print(raw_s1)
print(raw_s2)
print(raw_s3)
print(raw_s4)

# 멀티라인
multi_str1 = \
    """
    문자열
    멀티라인
    테스트
    """

# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)