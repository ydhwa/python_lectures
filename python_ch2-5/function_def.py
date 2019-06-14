def dummy():
    pass


def my_function():
    print('Hello World')


def times(a, b):
    return a * b


def none():
    return


def my_function2(func):
    func()


dummy()
my_function()
print(times(10, 20))
print(none())


# 함수도 객체이다.
print(dummy, type(dummy))
f = my_function
f()
my_function2(f)     # Java도 가능하긴 한데, 트릭을 써서 넘어가는 것처럼 보이게 하는 것이다. (lambda 식)

print(f, my_function)


# 여러 return 값. tuple 형으로 값의 묶음을 반환
def func():
    return 10, 'hello', {1, 2, 3}, (1, 2, 3)


n, s, st, t = func()
print(n, s, st, t)
