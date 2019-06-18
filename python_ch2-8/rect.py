# class Rect

class Rect:
    # x1 = 0      # 클래스 멤버임. 이렇게 선언하면 안됨
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Rect({0}, {1}, {2}, {3})'.format(self.x1, self.y1, self.x2, self.y2)

    # 비교 연산자 오버로딩
    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def draw(self):
        print('{0}를 그렸습니다.'.format(self))