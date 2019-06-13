# 무한루프
# while True:
#     ...

# random
import random

min, max = 1, 100
random.randrange(max) + min

while True:
    n = random.randrange(max) + min
    print(n)

    if 'y' != input('다시 하시겠습니까? [y/n]>> '):
        break

