# MyString class

class MyString:

    def __init__(self, s):
        self.s = s

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        if isinstance(other, MyString):
            return MyString(self.s + other.s)
        else:
            return self.s + other

    def __radd__(self, other):
        if isinstance(other, MyString):
            return MyString(other.s + self.s)
        else:
            return other + self.s

    def __mul__(self, other):
        return self.s * other

    def __neg__(self):
        return self.s[::-1]

    def __str__(self):
        return self.s


# 연산자 오버로딩(Operator Overloading)
# 연산자에 대해 클래스에 새로운 동작을 정의하는 것
# Python 에서는 사용하는 모든 연산에 대해 새롭게 정의할 수 있다.
s = MyString('Python Programmer is Good')

print(s / ' ')
print(s + ' Job')   # 오버로딩 되어 있지 않은 연산자 사용 시 오류가 발생한다.
print(MyString('python') * 3)

# 수치 단항 연산자 오버로딩
print(-MyString('Python '))

print(MyString('Hello') + MyString(' ') + MyString('World'))

# 역이항 연산자 오버로딩
print('Hello ' + MyString('World'))
