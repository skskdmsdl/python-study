# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n")) 
print(python.find("Java")) # -1 출력
print(python.index("Java")) # 에러남

print(python.count("n")) 