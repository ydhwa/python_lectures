# packing: tuple만 가능
t = 10, 20, 30, 'python'
print(t, type(t))

# unpacking
a, b, c, d = t
print(a, b, c, d)

# 에러
# a, b = t
# a, b, c, d, e, f = t
# 수를 맞춰줘야 한다.

# unpacking extended
t = (1, 2, 3, 4, 5)
a, *b = t
print(a, b)

a, *b, c = t
print(a, b, c)

# cf. 여러 개 파라미터를 받는 함수
def sum(*num):
    result = 0
    for i in num:
        result += i
    return result


print(sum())
print(sum(1, 2, 3))
print(sum(1, 2, 3, 4, 5, 6))


# c의 printf() 흉내내기
def printf(format, *args):
    print(format % args)


printf("name: %s, age: %d", "둘리", 10)


