# hello.py
def add(m, n):
    s = m
    s += n
    return s


def max(m, n):
    if m > n:
        return m
    else:
        return n


a = 2
b = 1

if a > 1:
    print('a가 1보다 큽니다.')
    print('a가 1보다 큽니다.')

    for i in range(1, 10):
        print('*' * i)

    if b == 1:
        pass

    print('^-^')


print(add(a, b))
print(max(a, b))

print('hello world')
