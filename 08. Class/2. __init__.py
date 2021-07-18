# __init__
# 파이썬에서 쓰이는 생성자
# 객체가 만들어질 때 자동으로 호출
# 객체는 마린이나 탱크와 같이 클래스를 통해 만들어지는 것들을 말함
# 또한 마린과 탱크는 Unit 클래스의 인스턴스라고 표현함

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