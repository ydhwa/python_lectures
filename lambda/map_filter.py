def f(x):
    return x ** 2


# map(f, [1, 2, 3, 4])

# map은 iterator 객체이다.
it = map(lambda x: print(x**2, sep=' '), [1, 2, 3, 4])
next(it)
next(it)
next(it)
next(it)
print('===========================')


# 만듦과 동시에 출력시키려면?
# list에 iterator를 인자로 주면 list가 알아서 next를 시켜(next를 시킨다면 그 과정에서 실행이 됨) 리스트에 넣는다.
lst = list(map(lambda x: x**2, [1, 2, 3, 4]))
print(lst)
print('===========================')


list(map(lambda x: print(x**2, sep=' '), [1, 2, 3, 4]))
print('\n===========================')


# filter
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
print('===========================')

