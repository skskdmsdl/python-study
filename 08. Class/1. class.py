# 클래스 

# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print(f"{name} 유닛이 생성되었습니다.")
print(f"체력 {hp}, 공격력 {damage}\n")

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print(f"{tank_name} 유닛이 생성되었습니다.")
print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")

# 공격 함수
def attack(name, location, damage):
	print(f"{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]")

attack(name, "1시" , damage) # 마린 공격 명령
attack(tank_name, "1시" , tank_damage) # 탱크 공격 명령

# 위의 코드를 클래스로 만들기(유닛 추가시마다 코드를 다 적지 않아도 됨)
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

### 추가 공부 ###
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언 
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
class UserInfo:
    def __init__(self, name): # init 메소드(필수)
        self.name = name

    def print_info(self):
        print("Name: " + self.name)

    def __del__(self):
        print("Instance removed!")

user1 = UserInfo("Kim")
user2 = UserInfo("Park")

print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print('user1 : ', user1.__dict__)  # 클래스 네임스페이스(창고) 확인
print('user2 : ', user2.__dict__)

print(user1.name)

# 예제2
# self의 이해

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")

f = SelfTest()
# print(dir(f))
print(id(f))
# f.function1() #예외 발생
f.function2()
print(SelfTest.function1())

# print(SelfTest.function2()) #예외 발생
print("dddd",SelfTest.function2(f))

# 예제3
# 클래스 변수(self 없음), 인스턴스 변수(무조건 self가 들어감)

class Warehouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Kim')
user2 = Warehouse('Park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)  # 클래스 네임스페이스 , 클래스 변수 (공유)

# Warehouse.stock_num = 50 # 직접 접근 가능

# 인스턴스 네임스페이스에 값이 없으면 클래스 네임스페이스에서 값을 가지고 옴
print(user1.stock_num) 
print(user2.stock_num)