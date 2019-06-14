# 레퍼런스 복사
# x의 변경은 곧 y의 변경과 같다.
import copy

a = 1
b = a

a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = x

print(x)
print(y)
print(x is y)       # True


# Swallow Copy(얕은 복사)
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.copy(x)

print(x)
print(y)
print(x is y)           # False
print(x[0] is y[0])     # True


# Deep Copy(깊은 복사)
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.deepcopy(x)

print(x)
print(y)
print(x is y)           # False
print(x[0] is y[0])     # False
print(x[2] is y[2])     # True


# 깊은 복사가 복합객체만을 생성하기 때문에
# 복합객체가 한 개만 있는 경우에는
# 얕은 복사, 깊은 복사의 차이는 없다.
a = ['hello', 'world']
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

a = ['hello', 'world']
b = copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])

