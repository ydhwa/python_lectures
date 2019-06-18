# class Point

class Point:
    count_of_instance = 0

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        # count_of_instance = 0           # Local Symbol Table
        # self.count_of_instance += 1     # 변수나 진배 없음. 인스턴스의 수를 카운팅하고 싶다면 아래와 같이 나타내자.
        Point.count_of_instance += 1

    def __del__(self):
        Point.count_of_instance -= 1

    def __str__(self):
        # return str(type(self)) + 'Point({0}, {1})'.format(self.x, self.y)
        return self.__repr__()

    def __repr__(self):
        # 반드시 이 모양으로 만들어줘야 한다. 객체로 재생이 가능한 문자열이어야 하기 때문
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # 확장 산술 연산자 오버로딩
    def __iadd__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # 인스턴스 메소드
    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def show(self):
        print(f'점[{self.x}, {self.y}]를 그렸습니다.')

    # 클래스 메소드
    @classmethod
    def class_method(cls):
        return cls.count_of_instance

    # 스태틱 메소드
    def static_method():
        print('static_method() 호출')

