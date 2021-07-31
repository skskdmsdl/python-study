# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가 
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다. --

# (활용 예제)
'''
from random import *

lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst) # 순서를 무작위로 바꾼다.
print(lst)
print(sample(lst, 1)) # 아무거나 1개만큼 추출
'''

from random import *

user_list = range(1, 21) # user_list에 1~20까지 숫자 생성
user_list = list(user_list)

shuffle(user_list) # 무작위로 순서를 바꿔줌

random_list = sample(user_list, 4) # user_list에서 4명을 추첨

chicken = random_list[0] # 치킨 추첨
coffee = random_list[1:] # 커피 추첨

print("-- 당첨자 발표 --")
print("치킨 당첨자 : ", chicken)
print("커피 당첨자 : ", coffee)
print("-- 축하합니다. --")

