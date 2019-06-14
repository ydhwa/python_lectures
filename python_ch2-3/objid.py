import sys

i1 = 10
i2 = 19
print(hex(id(i1)), hex(id(i2)))  # 같다.

i1 = 1234567890
i2 = 1234567890
print(hex(id(i1)), hex(id(i2)))  # 같다.

i1 = 11
i2 = 10 + 1
print(hex(id(i1)), hex(id(i2)))  # 같다.

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))  # 다르다.

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))  # 같다.

t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(hex(id(t1)), hex(id(t2)))  # 같다.
print(sys.getrefcount(t1), sys.getrefcount(t2))     # 왜 5나 나올까? (literal로 선언하면 내부적으로 뭔가 더 참조하고 있는 것이 있기 때문이 아닐까?)

t3 = tuple(range(1, 4))
print(sys.getrefcount(t3))
print(t1 is t3)

t4 = (0, 1, 2, 3)[1:]
print(t1 is t4)

# Immutable vs Mutable
# is (동일 레퍼런스 비교)
print(i1 is i2)
print(l1 is l2)
print(s1 is s2)
print(t1 is t2)

