# 치환문 예

a = 1
b = a + 1
print(a, b, sep=', ')

# 세미콜론으로 치환을 구분
# 2.x 대에서 나왔던 문법이므로 쓰지 않는 것을 권장
e = 3.5; f = 5.3
print(e, f)

# 여러 개를 한꺼번에 치환
e, f = 3.5, 5.3
print(e, f)

# 여러 개를 같은 값으로 치환
x = y = z = 10
print(x, y, z)

# 값 교환
e, f = f, e
print(e, f)

# C 형식은 허용되지 않음
# a = (b = c + d)

# 동적 타이핑
# 변수에 새로운 값이 할당되면 값을 버리고 새로운 값으로 치환된다.
a = 1
print(type(a))
a = 'hello'
print(type(a))

# 확장 치환문
a = 10
a += 10     # a = a + 10
print(a)

a -= 3
print(a)

a *= 2 + 3
print(a)

