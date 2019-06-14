def f():
    l_a = 2
    l_b = '마이콜'
    # 심볼 테이블 확인(Local)
    print(locals())


class MyClass:
    x = 10
    y = 20


# global
g_a = 1
g_b = '둘리'
f()
# 심볼 테이블 확인(Global)
# print(globals())


# 1. 정의된 함수
f.k = 'hello'
# 심볼 테이블 확인(Object)
print(f.__dict__)

# =========================


# 2. 클래스 객체
MyClass.z = 10
# print(MyClass.__dict__)


# 내장 함수는 심볼 테이블이 없다. 따라서 확장하지 못한다.
# print.x = 10              # X
# print(print.__dict__)     # X


# 내장 클래스는 심볼 테이블 있으나, 확장하지 않는다.
# str.z = 10        # X
print(str.__dict__)


# 내장 클래스로 생성된 객체
# 심볼 테이블이 없으므로 확장도 안된다.
# g_a.z = 10            # X
# print(g_a.__dict__)   # X


# 내장클래스와 내장함수는 심볼 테이블이 있으나 없으나 확장 금지이다.
# str.z                     # X
print(str.__dict__)
# print(print.__dict__)     # X


# 사용자 정의된 클래스로 생성된 객체
# 심볼 테이블이 없으므로 확장도 되지 않는다.
o = MyClass
o.z = 10
print(MyClass.__dict__)
# print(o, __dict__)        # X
