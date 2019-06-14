# 스코핑 룰(Scope)
# Local -> Global -> Built-in Scope 순으로 찾는다.

def func1(a):
    x = 2
    return a + x


# symbol table로 찾고, 시간 상 func가 늦게 실행되기 때문에 오류 없이 잘 발생한다.
def func2(a):
    return a + x


def func3(a):
    global g
    g = 3
    return a + g

x = 1

# (L)GB
print(func1(3))

# L(G)B
print(func2(3))
print(g)
print(func3(10))
print(g)

# LG(B)
print(dir('__builtins__'))