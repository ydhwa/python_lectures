# 1. Local
# 2. Enclosing Function(내포한 함수)
# 3. Global
# 4. Built-in


a = 1       # G
b = 300     # G
def f():
    b = 200     # E

    def g():
        b = 100     # L
        print(b)
        print(__name__)     # B. 지금은 __main__으로 나오지만 import되는 경우, 다른 내용이 출력된다.
    g()


# 단독으로 실행할 때만 f를 실행시키도록 한다.
if __name__ == '__main__':
    f()
