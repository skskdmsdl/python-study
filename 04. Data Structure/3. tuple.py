# 튜플(tuple)
# list와 다르게 내용 변경이나 추가가 불가능하지만 속도가 빠름

menu = ("돈까스", "치즈돈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 에러남

# name = "유재석"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("유재석", 20, "코딩")
print(name, age, hobby)