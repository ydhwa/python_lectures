# 객체의 대소의 비교

print(1 > 3)
print(2 > 4)

print(1 >= 3)
print(2 <= 4)

print(6 == 9)
print(6 != 9)

# 복합관계
a = 6
print(0 < a and a < 10)
print(0 < a < 10)


# 수치형 이외의 객체 비교
print('abcd' > 'abd')       # 문자열
print((1, 2, 4) < (1, 3, 1))        # 시퀀스
print([1, 3, 2] < [1, 2, 1])        # 리스트

# print([1, 3, 2] < (1, 2, 1))        # error. 다른 타입의 자료형 비교 불가
print([1, 3, 2] < list((1, 2, 1)))    # 형변환으로 해결

# 동질성 비교: ==  동질성 비교: is
a = 10
b = 20
c = a
d = 10
print(a == b)
print(a is b)
print(a is c)
print(a == c)
print(a is d)
print(a == d)

# 과연 list 자료형의 동일성과 동질성은?
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)     # 동질성은 다르다. (mutable과 immutable의 차이이다.)

# 논리의 계산 순서
# 빈 것은 False 취급
print([] or 'logical')          # logical
print('operator' or 'logical')  # operator
print('' or 'operator')         # operator
print('' and 'operator')        # operator
print(None and 1)
print(None or [])


# s = 'hello world'
def f(msg = None):
    msg and print(msg)


f()
f('hello world')


# def f():
#     print('execution!!!!!!!!!!!!')
# if 1 + 2 < 10:
#     f()
# 1 + 2 < 10 and f()

