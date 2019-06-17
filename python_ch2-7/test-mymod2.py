import mymod2
import mymod


# 한 모듈을 여러 번 import한다고 해도, 여러 번 메모리에 적재되지 않는다.
# 그러니 자유롭게 import하자.
print(mymod.add(10, 20))
print(mymod.subtract(10, 20))
print(mymod.multiply(10, 20))
print(mymod.devide(10, 20))

print(mymod2.power(10, 20))
