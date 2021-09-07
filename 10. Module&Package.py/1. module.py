# 모듈

# 모듈 사용법
# .을 사용하여 모듈 속 함수/변수 사용 => random.randrange(0, 5)

# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때 가격
# theater_module.price_soldier(5) # 5명이서 군인 할인 영화 보러 갔을 때 가격

# import theater_module as mv
# mv.price(3) # 3명이서 영화 보러 갔을 때 가격
# mv.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때 가격
# mv.price_soldier(5) # 5명이서 군인 할인 영화 보러 갔을 때 가격

# from theater_module import *
# price(3) 
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3) 
# price_morning(4)
# # price_soldier(5)

from theater_module import price_soldier as price
price(5) 
