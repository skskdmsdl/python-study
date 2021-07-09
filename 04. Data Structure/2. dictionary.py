# 사전

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # 에러 발생
print(cabinetget(5)) # None
print(cabinet.get(5, "사용 가능")) # 사용 가능

print(3 in cabinet) # True
print(6 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-100"] = "하하"
cabinet["C-20"] = "정형돈"
print(cabinet)

# 간 손님
del cabinet["A-100"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet) # {}
