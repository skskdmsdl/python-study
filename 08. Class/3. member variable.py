# 멤버 변수
# name, hp, damage와 같이 클래스 내에서 정의된 변수

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닛이 생성되었습니다.")
        print(f"체력 {hp}, 공격력 {damage}\n")

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5) # 체력 80, 공격력 5
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}") # 멤버변수 외부에서 접근

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.cloaking = True # 파이썬에서는 추가로 변수를 외부에서 만들어 사용 가능(확장), wraith2외에는 적용 안됨

if wraith2.cloaking == True: 
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")