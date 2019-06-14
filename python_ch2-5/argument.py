# 기본 인수값
def incr(a, step=1):
    return a + step


# def decr(step=1, a):
#     return a + step


print(incr(10))
print(incr(10, 3))
print(incr(10, step=10))
# decr(10)        # 이 경우, 파이썬이 이 값이 step인지 a인지 헷갈려서 런타임 오류를 낸다. (default값이 없는 parameter는 뒤쪽에 선언하는 것이 좋다.)


# 키워드 인수
def area(width, height):
    return width * height


print(area(10, 20))
print(area(width=10, height=20))
print(area(height=20, width=10))
print(area(10, height=20))
# 오류
# area(10, width=20)
# area(height=20, 10)


# 가변인수
def varg(a, *args):
    print(a, args)


varg(10)
varg(10, 1)
varg(10, 1, 2, 3, 4, 5)


# 가변인수 응용
def _print(*args, end='newline'):
    print(args, end)


_print('hello', 'world', 'your', 'welcome')
_print(10, end='tab')
_print(10, 'tab')


# 가변인수 응용 II c의 printf 흉내내기
def printf(format, *args):
    print(format % args)


printf('%s이 %d원짜리 %s를 입고 %s를 차고 노래를 한다.', '타잔', 100, '망토', '시계')


# 정의되지 않은 키워드 인수 처리하기
def f(width, height, **kw):
    print(width, height)
    print(kw)


f(10, 20)
f(10, 20, depth=10)
f(10, 20, depth=10, dimension=3)
# 오류
# f(10, 20, depth=30, 40)


def g(a, b, *args, **kw):
    print(a, b)
    print(args)
    print(kw)


g(10, 20)
g(10, 20, 30)
g(10, 20, c=60)
g(10, 20, 30, 40, 50, c=60, d=70)


# 튜플/사전 파라미터
def h(name, age, height):
    print(name, age, height)


h('줄리', 30, 170)
t = ('줄리', 34, 160)
h(t[0], t[1], t[2])
# DB 등으로 값 받아서 넘길 때 유용하게 쓸 수 있을 것 같다.
h(*t)

d = {'name': '줄리', 'age': 29, 'height': 158}
h(d['name'], d['age'], d['height'])
h(**d)      # key값이 파라미터와 완벽하게 일치해야 오류가 나지 않는다.

