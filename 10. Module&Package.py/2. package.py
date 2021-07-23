# 패키지
# 모듈들을 모아놓은 집합

import travel.thailand # 맨 뒤에는 모듈, 패키지만 가능(클래스나 함수는 안됨)
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from import에서는 클래스 가져오기 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# from random import *
from travel import * # __init__에 vietnam 모듈 설정 해줘야 오류 안남
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()