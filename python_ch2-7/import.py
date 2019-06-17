# import math
# print(math.sin(math.pi / 4), math.cos(math.pi / 4))


# from math import sin, cos, pi
# print(sin(pi / 4), cos(pi / 4))


# from math import sin, cos, pi
# from mymath import pi
# print(sin(pi / 4), cos(pi / 4))
# print(pi)       # 나중에 import한 것으로 덮어쓰기한다.


# 비추천
# from math import *
# print(sin(pi / 4), cos(pi / 4))


# import math as m
# from mymath import pi
# print(m.sin(m.pi / 4), m.cos(m.pi / 4))
# print(pi)   # 충돌도 막을 수 있음


# 특정 모듈의 경우, alias 이름이 정해져 있다.
# import pandas as pd
# import numpy as np


from math import sin as mysin, cos as mycos, pi as mypi
print(mysin(mypi / 4), mycos(mypi / 4))
